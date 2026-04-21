=========================================================
Readme.txt, updated May 2025.

Sub - 3 Seconds VoxCeleb (Sub3Vox)
The Hong Kong Polytechnic University (PolyU)
=========================================================

The Sub3Vox corpus of conversational speech has been designed to provide speech material for the development and evaluation of automatic text-dependent speaker recognition systems. 
The Sub3Vox1 corpus has been curated from VoxCeleb1, by the Hong Kong Polytechnic University in Hong Kong SAR, China.
Sub3Vox1 contains 4,594,817 short audio files from 1,250 speakers. Additional information regarding the speakers involved, and types of handset devices used, can be found in the sub3vox_meta.csv. They are the same as in VoxCeleb.

This file contains a brief description of the Sub3Vox1 Speech Corpus.


1. Reference
_____________

When publishing studies or results on the Sub3Vox1 corpus, please cite

@inproceedings{zuo2025sub,
  title={The Sub-3Sec Problem: From Text-Independent to Text-Dependent Corpus},
  author={Zuo, Ruichen and Lee, Kong Aik and Huang, Zilong and Mak, Man-Wai},
  booktitle={Proc. Interspeech 2025},
  pages={4003--4007},
  year={2025}
}

2. Content of the release
__________________________

     File Type: 

          .txt - Information file

          .pkl - File list and trial list

          .wav - Speech file

          .csv - Word content and ID information, speaker meta information

          The speech files are named according to the following pattern,

              Ng_sXXXX_YYYYY_AAAA_BBBB.wav
		
              where the one-digit string "N" represents the number of words in the phrase, in Sub3Vox1, N is an integer from 1 to 8, in Sub3Vox2, N ranges from 1 to 9,
		    the "g" character indicates the word,
		    the "s" character indicates the sentence,
		    the string "XXXX" varies from one digit to four digits, represents the ID of the sentence in its N-word phrases,
		    the five-digit string "YYYYY" represents the sub-session ID, which is the same as the sub-session ID in VoxCeleb,
		    the strings "AAAA" and "BBBB" vary from one digit to five digits, represents the start and end time in milliseconds of this utterance in the original VoxCeleb audio.
		    

3. Sub3Vox Directory and File Structure
________________________________________

     The Sub3Vox directory is organized as follows,

     ./Sub3Vox/  
          --> infos
                 eval1_file_list.lst
                 eval1_file_list.txt
                 eval2_file_list.lst
                 eval2_file_list.txt
		 trial_list_example.txt
                 eval1_trial_list_female.parquet
                 eval1_trial_list_male.parquet
                 eval2_trial_list_female.parquet
                 eval2_trial_list_male.parquet
                 gramdict.pkl
                 Readme.txt
                 sub3vox1_meta.csv
                 sub3vox1_meta.pkl
                 --> gramlist
                        gramlist_1g.csv
                        gramlist_2g.csv
                        gramlist_3g.csv
                        gramlist_4g.csv
                        gramlist_5g.csv
                        gramlist_6g.csv
                        gramlist_7g.csv
                        gramlist_8g.csv
                        gramlist_9g.csv

          --> eval1	# IMPORTANT NOTICE: eval1 is shown as "dev" in the address of trial lists
                 --> <SPEAKER_ID>
                        --> <SESSION_ID>
                               --> <SENTENCE_ID>_<SUB_SESSION_ID>_<START_TIME>_<END_TIME>.wav

          --> eval2	# IMPORTANT NOTICE: eval2 is shown as "test" in the address of trial lists
                 --> <SPEAKER_ID>
                        --> <SESSION_ID>
                               --> <SENTENCE_ID>_<SUB_SESSION_ID>_<START_TIME>_<END_TIME>.wav


     The speech data are organized according to the following hierarchy:

     /<CORPUS>/<SET>/id<SPEAKER_ID>/<SESSION_ID>/<SENTENCE_ID>_<SUB_SESSION_ID>_<START_TIME>_<END_TIME>.<EXTENSION>

     where,

          CORPUS         == sub3vox1
          SET            == eval1/eval2		# IMPORTANT NOTICE: shown as "dev"/"test" in the address of trial lists
          SPEAKER_ID     == 5 digits, 10001 to 11251
          SESSION_ID     == 11-digit alphanumeric mixed string
          SUB_SESSION_ID == 5 digits
          SENTENCE_ID    == Ng_sXXXX, N: 1 to 9, XXXX: 1 to 1999
          EXTENSION      == wav
     
     In the trial list, the first row defines the columns for each trial. Each subsequent row corresponds to a single trial in the following format:

     Label Directory1 Directory2 Directory3 DirectoryTest SameGramN
     
     where,

          Label         == TC/TW/IC/IW		# Target-Correct / Target-Wrong / Impostor Correct / Impostor Wrong
          Directory1    == path to the first enrollment utterance (among the three enrollments)
          Directory2    == path to the second enrollment utterance
          Directory3    == path to the third enrollment utterance
          DirectoryTest == path to the test utterance
          SameGramN     == indicates whether the enrollment and test utterances have the same number of words (N).
                    Examples:
                    - If both enrollment and test are 3-word phrases → SameGramN = 1_3. (1 = same N, 3 = value of N)
                    - If enrollment is 2-word phrase and test is 3-word phrase → SameGramN = 0_2_3. (0 = different N, 2 = N of enrollment, 3 = N of test)


4. Corpus Speaker Distribution
_______________________________

     Table 1: Ethnic distribution - eval1

	Ethnic group              #Male        #Female      #Total
        ___________________________________________________________

            USA               414(62.26%)  360(66.06%)   774(63.97%)
            UK                124(18.65%)  86(15.78%)    210(17.36%)
            Canada            28(4.21%)    24(4.40%)     52(4.30%)
            Australia         25(3.76%)    12(2.20%)     37(3.06%)
            India             14(2.11%)    11(2.02%)     25(2.07%)
            Norway            13(1.95%)    6(1.10%)      19(1.57%)
            Ireland           12(1.80%)    3(0.55%)      15(1.24%)
            Germany           4(0.60%)     5(0.92%)      9(0.74%)
            Italy             3(0.45%)     5(0.92%)      8(0.66%)
            NewZealand        6(0.90%)     2(0.37%)      8(0.66%)
            Mexico            4(0.60%)     2(0.37%)      6(0.50%)
            Sweden            1(0.15%)     4(0.73%)      5(0.41%)
            Russia            0(0.00%)     4(0.73%)      4(0.33%)
            Chile             2(0.30%)     1(0.18%)      3(0.25%)
            Croatia           2(0.30%)     1(0.18%)      3(0.25%)
            Denmark           1(0.15%)     2(0.37%)      3(0.25%)
            Netherlands       1(0.15%)     2(0.37%)      3(0.25%)
            Philippines       1(0.15%)     2(0.37%)      3(0.25%)
            Spain             1(0.15%)     2(0.37%)      3(0.25%)
            Switzerland       3(0.45%)     0(0.00%)      3(0.25%)
            China             1(0.15%)     1(0.18%)      2(0.17%)
            Poland            0(0.00%)     2(0.37%)      2(0.17%)
            Portugal          1(0.15%)     1(0.18%)      2(0.17%)
            Austria           0(0.00%)     1(0.18%)      1(0.08%)
            Brazil            0(0.00%)     1(0.18%)      1(0.08%)
            Guyana            0(0.00%)     1(0.18%)      1(0.08%)
            Iran              0(0.00%)     1(0.18%)      1(0.08%)
            Israel            0(0.00%)     1(0.18%)      1(0.08%)
            Pakistan          1(0.15%)     0(0.00%)      1(0.08%)
            Singapore         1(0.15%)     0(0.00%)      1(0.08%)
            SouthAfrica       1(0.15%)     0(0.00%)      1(0.08%)
            SriLanka          0(0.00%)     1(0.18%)      1(0.08%)
            Sudan             1(0.15%)     0(0.00%)      1(0.08%)
            TrinidadandTobago 0(0.00%)     1(0.18%)      1(0.08%)
        ______________________________________________________________
            All               665(54.96%)  545(45.04%)   1210(100.00%)


     Table 2: Ethnic distribution - eval2

	Ethnic group              #Male       #Female      #Total
        __________________________________________________________

            USA              17(68.00%)   8(53.33%)      25(62.50%)
            UK               3(12.00%)    2(13.33%)      5(12.50%)
            Ireland          1(4.00%)     2(13.33%)      3(7.50%)
            Canada           1(4.00%)     1(6.67%)       2(5.00%)
            France           0(0.00%)     1(6.67%)       1(2.50%)
            India            1(4.00%)     0(0.00%)       1(2.50%)
            Mexico           1(4.00%)     0(0.00%)       1(2.50%)
            Norway           0(0.00%)     1(6.67%)       1(2.50%)
            Spain            1(4.00%)     0(0.00%)       1(2.50%)
        ___________________________________________________________
            All              25(62.50%)   15(37.50%)    40(100.00%)


