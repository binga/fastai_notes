Summary of all the versions
===========================

| Version | Local CV score | Public score | Private score | Rank (private) | GPU RAM* | Approach                                                                                    |
|---------|----------------|--------------|---------------|----------------|----------|---------------------------------------------------------------------------------------------|
| v1      |  will update this    | 0.92443        | -             | -              | ~2548MB      | [resnet50](https://github.com/KaimingHe/deep-residual-networks), top-down trafo, mostly fastai defaults - cyclical lr + differential lr - with unfreeze. |
| v3      |  0.9709    | 0.97858        | -             | -              | ~2548MB      | [resnet50](https://github.com/KaimingHe/deep-residual-networks), top-down trafo, mostly fastai defaults - cyclical lr + differential lr - [1e-5, 1e-3, 1e-1] + TTA |
| v4      |  0.9812    | 0.98110        | -             | -              | ~2548MB      | [resnet50](https://github.com/KaimingHe/deep-residual-networks), top-down trafo, mostly fastai defaults - cyclical lr + differential lr - [1e-4, 1e-2, 1e-1] plus [1e-18, 1e-12, 1e-10] + TTA |

* **GPU RAM**: This heavily depends on size of the input image being processed and the batch size. Please go through the code to see the parameters used.
