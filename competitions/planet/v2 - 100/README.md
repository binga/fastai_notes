## Model Score on Kaggle Leaderboard

Public: 0.93095 | Private: 0.92898 (100/938 - Top 11%)

## Approach
1. Setup a 3 - fold CV
2. Take a pretrained resnet34 model. Apply top down transformations for data augmentation.
3. Find an optimal learning rate using cyclical learning rates.
4. Train it for a couple of epochs. Remember only the last dense layers are trained.
5. Unfreeze all the layers.
6. Use differential learning rates to train each layer on the convnet. Find out CV score.
7. Use steps 2-6 to train on complete dataset and extract predictions on test set.
