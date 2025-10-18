# pro1-pam-hw2-114753210PengPeiRong
NCCU Bioinformatics hw2 - Calculate the Sum-of-Pair score
可以直接參考與ChatGPT的對話：https://chatgpt.com/share/68f39e9e-15d4-800b-802a-3943b3ec3c5c

一、首先我將手邊的資料都提供給ChatGPT（包含上課的兩份簡報，topic04_msaCom和topic05_appMsa，以及作業說明README、程式碼開頭hw2_ref.py，還有四份檔案pam100.txt、pam250.txt、test1.fasta、test2.fasta）。我告訴ChatGPT我是computer science的學生，修讀生物資訊概論與實務，我想請教它關於程式作業2pro2.SoP-MSA該怎麼做。

Prompt1：
我是computer science的學生，修讀生物資訊概論與實務，我想請教你關於程式作業2pro2.SoP-MSA該怎麼做，我會提供給你上課簡報（topic04_msaCom.pdf和topic05_appMsa.pdf）以便讓你參考。
我接下來會告訴你作業的已知及需求，請你幫助我完成本次的程式作業。
1.程式作業要求如下：Write Python script to calculate the Sum-of-Pair score of the alignment。
2.程式碼撰寫的開頭為【def calculate_SoP(input_path, score_path, gopen, gextend):】（與hw2_ref.py的程式碼內容相同）
3.此次作業提供的資訊有README.md，我將文字的部分附在"第4點"給你；還有程式碼開頭hw2_ref.py（我已在"第2點"提供給你）；還有提供兩個.txt檔案，分別是pam100.txt、pam250.txt；以及兩個.fasta檔案，分別為test1.fasta、test2.fasta。
4.README的內容我有附在提供給你的檔案中（＊並貼上README在指令中給ChatGPT）

二、閱讀完後確認一下本次程式作業目的、各個檔案用途，並請ChatGPT建議流程給我。（途中若ChatGPT有提供測試給我，我都會測試確認答案是否正確，如果不確定就將測試結果貼給ChatGPT請他協助確認。例如Prompt6~7的回覆中有測試程式的需求，我就會在下次提問一併確認剛才的測試是否正確。）

Prompt2：
1.請先幫我將README的內容翻成繁體中文讓我確定題目意涵及目的。 2.接下來告訴我各個檔案的用途。 3.告知我檔案用途後告訴我，你建議我的流程/步驟。

3.接著請ChatGPT，一步一步地教我怎麼做，每次都要提供截至目前為止的所有程式碼，並且說明背後意涵。
Prompt3：請你按照步驟告訴我該如何撰寫程式碼及背後的意義。
Prompt4：請你用上面的邏輯，一步步教我寫出 hw2.py 的完整程式，並在每一段加上分別用中英文註解說明「它在生物上代表什麼」。 每告訴我一步驟就要列出從頭到尾的完整程式碼給我。
Prompt5：請繼續Step2（讀 PAM matrix 的生物邏輯 + 程式碼）
Prompt6：互動環境測試正確。請繼續Step3 處理 讀取 FASTA 檔（MSA 序列）。 （＊這邊有測試ChatGPT提供的測試）
Prompt7：1.剛剛測試結果如下，我要如何判斷是否正確? （＊並貼上測試結果）　2.請繼續Step 4：計算 column 內的兩兩配對分數 (pairwise scoring)
Prompt8：請繼續Step 5（驗證第二組測試test2.fasta + pam100.txt，並加上簡單的 main 測試區塊方便執行。）

三、ChatGPT提供完整程式碼，但結果不符合，在前面的測試中有發現錯誤，ChatGPT認為是「沒有新增gap open penalty」的緣故，因此接下來我要請他新增「gap open penalty」來改良程式碼。
Prompt9：所以現在可以新增gap open penalty來改良結果對吧?是的話請繼續 Step 6（改良 gap penalty 邏輯，讓分數正確）
Prompt10：我直接執行你上面的程式碼，出現結果如下，與答案不符。

四、發現結果仍錯，接結果貼給ChatGPT後，它告訴我：原因應該是「gap open 沒被正確偵測」造成的。」先前in_gap 狀態是以「欄」為單位記錄整條序列的 gap 狀態，但在 多序列 pairwise 比對 時，gap open 應該以「每一對序列」為基準獨立追蹤，而不是全域共用。

五、將本次提供的程式碼執行，發現Test1結果正確了，於是我於Prompt11先理解剛才修正的內容及邏輯，在於Prompt12中告訴ChatGPT剛才的結果。
Prompt11：請問你剛剛做了什麼修正?具體改變為何?程式碼改變了哪裡?
Prompt12：好的我理解了，但剛剛的結果如下，與Test 2結果還是不符。

六、由於執行ChatGPT更正後的新程式碼還是錯誤，因此我請GPT告訴我Test2相關的城市程式碼的意義、觀念、及邏輯。
Prompt13：答案還是錯的我想找原因，所以請告訴我與test2相關的程式碼中，程式碼的意義、觀念、及邏輯。

七、在自己重新閱讀完程式碼後我發現test1的gap open / gap extend在特定情況很像會算成兩次，所以請GPT修正；在執行pro1時有遇過問題是讀取pam.txt檔案時資料分割錯誤導致結果一直失敗，所以我重新貼了pam100.txt和pam250.txt的內容於prompt裡，並附上截圖給GPT，請GPT幫我修改程式碼，改用pandas的方式讀取檔案。
Prompt14：
1.test1的gap open / gap extend在特定情況很像會算成兩次，我希望修正成不會重複計分。
2.test2的部分，我在想有沒有可能跟上次作業遇到的問題一樣，問題有沒有可能是出在讀取或分割資料。我上次有用到numpy跟pandas（import numpy as np 、import pandas as pd），請你協助我將讀取pam的方法變成pandas。

八、再次交涉幾次後，發現Test2結果還是有誤，因此我詢問GPT我提供哪些資料給它會讓它比較好幫助我修正問題。
Prompt15：結果如下，可以看到test2還是出錯，我該提供甚麼資料給你，以便你協助我幫我修正問題。（並貼上此次結果）
  ChatGPT回覆：
  超清楚，感謝你把狀況貼出來！我直接把「你手上的檔案」算了一遍並檢查結構，結論是：

  你的 examples/test2.fasta 有2 條序列、長度 381（每條），其中
  202 欄是胺基酸–胺基酸、1 欄是單邊 gap、178 欄是雙邊 gap。

  用你附的 pam100.txt 計算，202 個胺基酸–胺基酸欄位的 PAM 分數總和 = 1180。
  只有 1 個單邊 gap → 只會產生 1 次 gap open = -8（沒有 extend）。
  所以 SoP = 1180 - 8 = 1172。
  這與你看到的 1172 完全一致。

  也就是說：以你現在的檔案與題目說的 scoring 規則（PAM + affine gap）來算，1172 是數學上唯一合理的答案。要把它變成 606，就必須「改規則」或「換資料」。

九、根據GPT提供的測試，我發現是採納不同的「評分規則」，因此結果一直不同，GPT也提供幫助我診斷如何加分的程式碼給我，於是我執行GPT提供的程式碼，並再提供結果給GPT。
Prompt16：
1.我的檔案都是下載正確的，所以test2.fasta 一定跟老師同一版，至於你叫我檢查，結果也證明兩者相同，結果如下 len: 381 ll: 202 -l: 1 l-: 0 --: 178 
2.至於第2點你說【老師的評分規則是否「把 '--' 欄位也扣分」】我不確定所以我先不動作。 
3.我執行你的「診斷版」及【debug_sop("examples/test2.fasta", "examples/pam100.txt", -8, -2, max_rows=40) 】程式碼後結果如下（附上結果於prompt中並附圖）

  ChatGPT回覆：
  太好了，你把證據都貼清楚了—現在可以把「為什麼你算到 1172，而老師公佈是 606」這件事具體化。
  【快速結論（先說重點）】
    ．你的 test2.fasta 與我推導的一樣：381 欄；其中 AA/AA=202、單邊 gap=1、雙邊 gap=178。
    ．以「AA/AA 用 PAM100、單邊 gap 只扣一次 gopen=-8、-- = 0」來算 → 202 欄 PAM 總和 1180 − 8 = 1172。 這就是你現在得到的數字，完全合理。
    ．要把 1172 降到 606，必須對 --（雙邊 gap）另外扣分。差額是 1172 − 606 = 566，剛好來自大量 -- 欄位。

  【推論老師規則（可被資料驗證）】
  如果把每一段連續的 -- 視為「一段 gap」，並且：
  ．雙邊 gap 也要懲罰，但只算一次（就像把 -- 當成一邊有 gap、另一邊是空白）：
    ．該段開始：扣 gopen
    ．該段之後每個 --：扣 gextend
  那麼，對長度為 L 的 -- 區塊，懲罰 = gopen + (L-1)*gextend。
  把所有 -- 區塊加總（共有很多段），就是額外要扣的總分。
      用你的參數 gopen=-8, gextend=-2，一段長度 L 的雙邊 gap 會額外扣：　-8 + (L-1)*(-2) = -2L - 6。
  為了把 1172 拉到 606，需要額外扣 566。
  把 178 個 -- 分布在 r 段 連續區塊，總扣分 = Σ(-2L_i - 6) = -356 - 6r。
  套入方程：1172 + (-356 - 6r) = 606 → 816 - 6r = 606 → r = 35。
  
  也就是說：如果 test2 的 -- 恰好切成 35 段連續區塊，用這個規則就會得到 606。這不是碰運氣；這是可驗證的。

  【你馬上可跑的「驗證小程式」】
  用它來數一數 -- 的連續區塊數 r 與 總長 178 是否吻合。如果 r=35，就百分之百證明老師採用的是「雙邊 gap 視為單邊 gap 的 affine 懲罰」。
  （驗證的程式碼）
  【直接給你「可切換規則」的 SoP 計算】
  我把 -- 的處理做成 mode 參數，三種常見規則你都能一鍵切換：
  "affine_no_gg"：-- 不計分（你現在得到 1172 的版本；test1=1047 OK）
  "affine_gg_as_single"：把 -- 視為「單邊 gap」的一段，段首扣一次 gopen，後續每格扣 gextend（最可能導出 606）
  "sp_nogap"：只有 AA/AA 計 PAM，任何帶 - 的欄位都不計（有時作業會用這個）
  把下面函式放進你現有的 hw2.py（你 pandas 讀 PAM 與 read_fasta 保持不變）：(*程式碼)
  然後在主程式測三個模式：(測試程式碼)

  如果你看到 affine_gg_as_single = 606，那就與老師一致 ✅

十、我將執行ChatGPT提供的驗證程式碼的結果貼給GPT
Prompt17：
1.你提供給我的馬上可跑的「驗證小程式」的結果為【double-gaps = 178 blocks = 35】
2.我把你要我加入的def calculate_SoP_with_mode加入程式碼並執行你要我執行的結果後出現結果如下: 
  — Test1 — 
  affine_no_gg: 1047 
  — Test2 — 
  affine_no_gg: 1172 
  sp_nogap: 1180 
  affine_gg_as_single: 606

  ChatGPT回覆：
  太讚了！你已經把關鍵證據都跑出來了👏
  double-gaps = 178, blocks = 35
  三種模式的分數：affine_no_gg=1172、sp_nogap=1180、affine_gg_as_single=606
  這完全說明：老師的評分規則是把 --（雙邊 gap）視為一段 gap 來懲罰：段首扣 gopen，續列扣 gextend。
  所以我們把最終作業版統一採用這個規則就能同時通過 test1 與 test2。

十一、在確認Test1、Test2結果與老師提供的分數相同後我詢問GPT還有其他方法可以測試答案正確性嗎?附上程式碼給我，並幫我確認結果是否正確。以及詢問剛剛是如何檢查出規則不同的?三種規則哪裡不同?
Prompt18：
1.除了老師提供的測試外，我有辦法測試這份程式碼是否正確嗎? 2.請告訴我你是如何檢查出規則的不同的?三種規則差在哪?
Prompt19：
請幫我附上一個超精簡「單元測試集（5~6 個迷你 FASTA）」的小檔，讓我一鍵跑完所有規則與期望分數，當回歸測試。
Prompt20：
mini_tests.py的結果如下，請你幫我檢查（複製、貼上結果給GPT）。
