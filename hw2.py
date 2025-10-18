# hw2.py
# Name: 彭珮蓉
# Student ID: 114753210
# -------------------------------------------------------
# Calculate Sum-of-Pairs (SoP) for a given MSA.
# Rule: affine gap for single-sided gaps, AND treat `--`
#       (double gaps) as one gap segment: open once, then extend.
# References: see README (ChatGPT assistance on SoP scoring & implementation.)
# -------------------------------------------------------

import pandas as pd

# ---------- Matrix Reader (robust, no guessing) ----------
def read_score_matrix_pd(score_path: str) -> pd.DataFrame:
    """
    Strictly parse a PAM-like matrix file.

    - Skip lines starting with '#'
    - First non-comment row is the column header (A R N ... *)
    - Each subsequent row: first token is row label; remaining tokens are ints

    Returns
    -------
    pandas.DataFrame
        DataFrame with string index/columns and int values.
    """
    header = None
    rows = []

    with open(score_path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if header is None:
                header = line.split()
                continue
            parts = line.split()
            row_label = parts[0]
            values = list(map(int, parts[1:]))
            if len(values) != len(header):
                raise ValueError(
                    f"Row {row_label} length {len(values)} != "
                    f"header length {len(header)}"
                )
            rows.append((row_label, values))

    if header is None or not rows:
        raise ValueError("Matrix file is empty or malformed.")

    df = pd.DataFrame(
        [v for _, v in rows],
        index=[r for r, _ in rows],
        columns=header,
    ).astype(int)
    return df

# ---------- FASTA Reader (aligned MSA with '-') ----------
def read_fasta(input_path: str):
    """
    Read an aligned FASTA (MSA) and return a list of sequences (with '-').

    All sequences must have the same length.
    """
    seqs, cur = [], []

    with open(input_path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            if line.startswith(">"):
                if cur:
                    seqs.append("".join(cur))
                    cur = []
            else:
                cur.append(line.replace(" ", ""))
        if cur:
            seqs.append("".join(cur))

    if not seqs:
        raise ValueError("No sequences found in FASTA.")

    L = len(seqs[0])
    if any(len(s) != L for s in seqs):
        raise ValueError("All sequences in the MSA must have equal length.")

    print(f"Loaded {len(seqs)} sequences, each of length {L}.")
    return seqs

# ---------- Core SoP (teacher rule) ----------
def _sop_affine_with_double_gap_blocks(
    seqs, score_mat_df, gopen: int, gextend: int
) -> int:
    """
    Teacher rule:

    - AA vs AA    : add PAM score
    - AA vs '-'   : affine gap (open once, then extend)
    - '-' vs '-'  : treated as an affine gap *block*;
                    first column pays gopen, subsequent columns pay gextend.

    中文：'--' 視為一段 gap，段首扣開啟，之後扣延伸。
    """
    n = len(seqs)
    L = len(seqs[0])
    total = 0

    # Track previous chars and whether a pair is inside a '--' block
    prev_chars = {(i, j): (None, None) for i in range(n - 1) for j in range(i + 1, n)}
    in_gg_block = {(i, j): False for i in range(n - 1) for j in range(i + 1, n)}

    for pos in range(L):
        for i in range(n - 1):
            for j in range(i + 1, n):
                a = seqs[i][pos]
                b = seqs[j][pos]
                prev_a, prev_b = prev_chars[(i, j)]

                # case 1) double-gap '--' -> treat as one gap segment
                if a == "-" and b == "-":
                    if not in_gg_block[(i, j)]:
                        total += gopen  # block starts
                        in_gg_block[(i, j)] = True
                    else:
                        total += gextend  # block extends
                    prev_chars[(i, j)] = ("-", "-")
                    continue

                # leaving a '--' block (if any)
                in_gg_block[(i, j)] = False

                # case 2) single-sided gap: penalize only the gapped side
                if a == "-" and b != "-":
                    total += (gextend if prev_a == "-" else gopen)
                    prev_chars[(i, j)] = ("-", b)
                    continue
                if a != "-" and b == "-":
                    total += (gextend if prev_b == "-" else gopen)
                    prev_chars[(i, j)] = (a, "-")
                    continue

                # case 3) AA vs AA: PAM lookup
                total += int(score_mat_df.loc[a, b])
                prev_chars[(i, j)] = (a, b)

    return total

# ---------- Public API (required by the assignment) ----------
def calculate_SoP(input_path: str, score_path: str, gopen: int, gextend: int) -> int:
    """
    Calculate the Sum-of-Pairs score under the teacher's rule:

    - AA/AA uses substitution matrix (PAM)
    - single-sided gaps use affine penalties
    - double gaps ('--') are penalized as an affine block (open once, extend thereafter)
    """
    score_mat = read_score_matrix_pd(score_path)
    print("Substitution matrix loaded successfully.")

    seqs = read_fasta(input_path)
    print("FASTA alignment loaded successfully.")

    total = _sop_affine_with_double_gap_blocks(seqs, score_mat, gopen, gextend)
    print(f"Sum-of-Pairs score = {total}")
    return total

# ---------- Quick tests ----------
if __name__ == "__main__":
    print("— Test1 —")
    s1 = calculate_SoP("examples/test1.fasta", "examples/pam250.txt", -10, -2)
    print("Expected 1047, got:", s1, "\n")

    print("— Test2 —")
    s2 = calculate_SoP("examples/test2.fasta", "examples/pam100.txt", -8, -2)
    print("Expected 606, got:", s2)
