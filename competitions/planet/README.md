Summary of all the versions
===========================

| Version | Local CV score | Public score | Private score | Rank (private)    | Approach                                                                                           |
|---------|----------------|--------------|---------------|-------------------|----------------------------------------------------------------------------------------------------|
| v1      | 0.93251 (3)    | 0.92990      | 0.92808       | 129/938 - Top 14% | resnet34, top-down trafo, cyclical lr - 0.05 on last layer, diff lr - 0.1, 6 epochs with unfreeze. |
| v2      | 0.93251 (3)    | 0.93095      | 0.92898       | 100/938 - Top 11% | v1 + train on full data                                                                            |
