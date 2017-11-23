Summary of all the versions
===========================

| Version | Local CV score | Public score | Private score | Rank (private) | GPU RAM* | Approach                                                                                    |
|---------|----------------|--------------|---------------|----------------|----------|---------------------------------------------------------------------------------------------|
| v1      | 0.550 (val)    | -            | -             | -              | 1GB      | [resnet34](https://github.com/KaimingHe/deep-residual-networks), side-on trafo, cyclical lr - 0.01 on last layer, differential lr - with unfreeze. |
| v2      | 0.479 (val)    | -            | -             | -              | 1.5GB      | [resnet50](https://github.com/KaimingHe/deep-residual-networks)                                                                                    |
| v3      | 0.39 (val)     | -            | -             | -              | 1.9GB     | [resnet152](https://github.com/KaimingHe/deep-residual-networks)                                                                                   |
| v4      | 0.285 (val)     | -            | -             | -              | 2.4GB     | [resnext101_64](https://github.com/facebookresearch/ResNeXt) + 0.5 dropout. Unfreezing massively overfits!                                                                                 |


* **GPU RAM**: This heavily depends on size of the input image being processed and the batch size. Please go through the code to see the parameters used.
