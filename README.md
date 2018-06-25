# Germanic phonetic/phonological transcription

### Available languages
Old Norse, Old Swedish and Gothic are available to be phonetically transcribed.

.. code-block:: python

  In [1]: from phonetics import *
  
  In [2]: import gothic, old_swedish, old_norse
  
  In [3]: example_sentence = "Anastodeins aiwaggeljons Iesuis Xristaus sunaus gudis."
  
  In [4]: tr = Transcriber(gothic.DIPHTHONGS_IPA, gothic.DIPHTHONGS_IPA_class, gothic.IPA_class, gothic.gothic_rules)
   
  In [5]: tr.main(example_sentence)
      [anastoːðiːns ɛwaŋgeːljoːns jeːsuis kristɔs sunɔs guðis]"
      
  In [6]: sentence = "Far man kunu oc dör han för en hun far barn. oc sigher hun oc hænnæ frændær."

  In [7]:  tr = ut.Transcriber(old_swedish.DIPHTHONGS_IPA, old_swedish.DIPHTHONGS_IPA_class, old_swedish.IPA_class,
                        old_swedish.old_swedish_rules)
  In [8]: tr.main(sentence)

  Out [8]: "[far man kunu ok dør han før ɛn hun far barn ok siɣɛr hun ok hɛnːɛ frɛndɛr]"
  
  In [9]: from cltk.phonology.old_norse import transcription as ont

  In [10]: sentence = "Gylfi konungr var maðr vitr ok fjölkunnigr"

  In [11]: tr = ut.Transcriber(ont.DIPHTHONGS_IPA, ont.DIPHTHONGS_IPA_class, ont.IPA_class, ont.old_norse_rules)

  In [12]: tr.main(sentence)

  Out [13]: "[gylvi kɔnungr var maðr vitr ɔk fjœlkunːiɣr]"
  
  
