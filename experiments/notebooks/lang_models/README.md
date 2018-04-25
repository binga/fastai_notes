Language Model for Telugu (Indian) Language
===========================================

This folder contains relevant files for creating a language model for the Telugu language from the Telugu Wikipedia corpus. The model used for the language model is the [AWD-LSTM model](https://github.com/salesforce/awd-lstm-lm) that produces the state of the art performance on the English language, by Salesforce Research. Additional information and the larger goal of the project is here: https://docs.google.com/document/d/1KtwqGcWe0JEzJlI43sAkLRnZrPTRBMCbjE-Q355hkvw/edit?usp=sharing


TODO:
- [ ] Host the language model weights for the community to reuse the model directly
- [ ] Use the [sentencepiece tokenizer](https://github.com/google/sentencepiece)
- [ ] Finetune
- [ ] Use continuous cache pointer (from here: https://github.com/salesforce/awd-lstm-lm)
- [ ] Try QRNN (from here: https://github.com/salesforce/pytorch-qrnn/)
- [ ] Identify new datasets for sentiment analysis.
- [ ] Figure out if there are any summarization datasets out there.
