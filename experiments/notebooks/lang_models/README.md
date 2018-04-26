Language Model for Telugu (Indian) Language
===========================================

This folder contains relevant files for creating a language model for the Telugu language from the Telugu Wikipedia corpus. The model used for the language model is the [AWD-LSTM model](https://github.com/salesforce/awd-lstm-lm) that produces the state of the art performance on the English language, by Salesforce Research. Additional information and the larger goal of the project is here: https://docs.google.com/document/d/1KtwqGcWe0JEzJlI43sAkLRnZrPTRBMCbjE-Q355hkvw/edit?usp=sharing

Language model weights are available for download [here](https://drive.google.com/file/d/1fjEJ__5WjClY6b1NB19gcWWx7md-rAC_/view?usp=sharing) and the itos (index -> string) mapping pickle file is available for download [here](https://drive.google.com/file/d/1s6treSTQYVTAsj6FXUSqyS96pA3X5NOO/view?usp=sharing)

TODO:
- [x] Host the language model weights and itos (index -> string vocab pickle file) for the community to reuse the model directly
- [x] Add gradient clipping
- [ ] Include the text generation code snippet to visually inspect language model (In progress)
- [ ] Use the [sentencepiece tokenizer](https://github.com/google/sentencepiece)
- [ ] Finetune
- [ ] Use continuous cache pointer (from here: https://github.com/salesforce/awd-lstm-lm)
- [ ] Try QRNN (from here: https://github.com/salesforce/pytorch-qrnn/)
- [ ] Identify new datasets for sentiment analysis.
- [ ] Figure out if there are any summarization datasets out there.
