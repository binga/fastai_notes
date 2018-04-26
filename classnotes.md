## fastai class running notes
=============================

The following notes contains some important points that I wanted to note during Jeremy's class as well as some exercises that Jeremy suggests during class - for research purposes.

Lesson - 11
- Backbone in usual models is similar to an encoder in machine translation
- 16th minute - mck problem.
- Create a 2-layer RNN
- Try converting dates of different formats to one single format (Maybe Borde's data cleaning exercise too)
- if your language doesn't have spaces, you should look at sentence piece for tokenization related things
- 34th minute - publishing papers of seq2seq models using language models
- 39th minute - adaptive pooling - varied size images
- Decoder works better if prepad=False for translation
- instacard kaggle problem - maybe work on it
- coupon recommendation - try modeling it on seq2seq on it
- pytorch padding weird - pair
- attention weights pytorch graph

Lesson - 12
- Come up with the mean and std of the images in CIFAR
- Images are too small for transforms_side_on
- Reflection padding
- Use inplace and func_ in pytorch to save memory
- Try running CIFAR on keeping the same number of channels in ResLayer
- GANs
- Try using adaptive average pooling layer in DCGAN_D in the end
- preact_resnet --> bn(relu(conv(x)))
- There's no point improving the generator if the discriminator doesn't perform well
- problems: mode collapse, memorizing the input


Lesson - 13
- Densenet is similar to resnet except that when merge happens, it's a concat
- Revisit the 7x1 and 1x7 conv again. Factored convolutions
- Standard resnet on top of inception stem.
- progressive gans paper uses
- runaway feedback loops in predictive policing
- content loss == perceptual loss
- VV - you dont need gradients for the input
- Jacobian - first derivative, hessian - second derivative
- try style transfer with sgd
- try half precision floating point
- Try doing gatys style transfer just doing diagonal of the gram matrix
