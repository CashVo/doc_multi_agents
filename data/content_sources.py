
conceptual_urls = [
    "https://pytorch.org/tutorials/beginner/basics/intro.html",
    "https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html",
    "https://pytorch.org/tutorials/beginner/nn_tutorial.html",
    "https://pytorch.org/tutorials/intermediate/nlp_from_scratch_index.html",
    "https://pytorch.org/tutorials/intermediate/tensorboard_tutorial.html",
    "https://pytorch.org/tutorials/intermediate/pinmem_nonblock.html",
]

tutorial_urls = [
    "https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html",
    "https://pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html",
    "https://pytorch.org/tutorials/beginner/basics/data_tutorial.html",
    "https://pytorch.org/tutorials/beginner/basics/transforms_tutorial.html",
    "https://pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html",
    "https://pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html",
    "https://pytorch.org/tutorials/beginner/basics/optimization_tutorial.html",
    "https://pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html",
    "https://pytorch.org/tutorials/advanced/custom_ops_landing_page.html",
]


# We will use the TorchText library for this purpose
api_urls = [
    "https://pytorch.org/text/stable/nn_modules.html",
    "https://pytorch.org/text/stable/data_functional.html",
    "https://pytorch.org/text/stable/data_metrics.html",
    "https://pytorch.org/text/stable/data_utils.html",
    "https://pytorch.org/text/stable/datasets.html",
    "https://pytorch.org/text/stable/vocab.html",
    "https://pytorch.org/text/stable/utils.html",
    "https://pytorch.org/text/stable/transforms.html",
    "https://pytorch.org/text/stable/functional.html",
    "https://pytorch.org/text/stable/models.html"
]

# Pytorch does not maintain a glossary of terms page so we will need to generate one ourselves
glossary_terms = {
  "terms": [
    {
      "term": "Tensor",
      "definition": "The primary data structure in PyTorch, similar to NumPy arrays but with GPU support, for performing various numerical operations."
    },
    {
      "term": "Autograd",
      "definition": "A core PyTorch feature enabling automatic differentiation for building and training neural networks."
    },
    {
      "term": "Backpropagation",
      "definition": "An algorithm to compute gradients of loss with respect to model parameters, used in training deep learning models."
    },
    {
      "term": "Gradient Descent",
      "definition": "An optimization algorithm for minimizing the loss function by adjusting model parameters iteratively."
    },
    {
      "term": "Module",
      "definition": "A PyTorch class (`torch.nn.Module`) that serves as the base class for all neural network layers and models."
    },
    {
      "term": "Optimizer",
      "definition": "A PyTorch utility (`torch.optim`) that updates model parameters based on computed gradients, commonly using methods like SGD or Adam."
    },
    {
      "term": "Loss Function",
      "definition": "A function that calculates the difference between predicted and actual values, guiding the training process."
    },
    {
      "term": "DataLoader",
      "definition": "A PyTorch class (`torch.utils.data.DataLoader`) for loading and batching data during training and testing."
    },
    {
      "term": "Dataset",
      "definition": "An abstraction representing a dataset, often used with `DataLoader` to manage data for training or inference."
    },
    {
      "term": "Convolutional Neural Network (CNN)",
      "definition": "A neural network type optimized for image processing, using convolutional layers to learn spatial hierarchies."
    },
    {
      "term": "Recurrent Neural Network (RNN)",
      "definition": "A neural network type suited for sequential data like time series or language, using feedback loops to maintain information across inputs."
    },
    {
      "term": "Transfer Learning",
      "definition": "A technique to leverage a pre-trained model on a new but similar task, allowing for faster and more effective training."
    },
    {
      "term": "Batch Normalization",
      "definition": "A layer that normalizes inputs to a layer, improving model stability and accelerating training."
    },
    {
      "term": "Dropout",
      "definition": "A regularization technique that randomly 'drops' units during training to prevent overfitting."
    },
    {
      "term": "Activation Function",
      "definition": "A function applied to neurons to introduce non-linearity, such as ReLU, Sigmoid, or Tanh."
    },
    {
      "term": "Epoch",
      "definition": "One complete pass through the entire training dataset during model training."
    },
    {
      "term": "Batch",
      "definition": "A subset of the dataset processed at one time, allowing for more efficient computation and memory usage during training."
    },
    {
      "term": "Learning Rate",
      "definition": "A hyperparameter that controls the step size in gradient descent updates, affecting training speed and convergence."
    },
    {
      "term": "CUDA",
      "definition": "A parallel computing platform by NVIDIA, enabling PyTorch to perform computations on GPUs."
    },
    {
      "term": "Fine-Tuning",
      "definition": "A transfer learning method involving slight adjustments to a pre-trained model's parameters on a new dataset."
    }
  ]
}

content_sources = {
    "conceptual_content": conceptual_urls,
    "tutorial_content": tutorial_urls,
    "api_content": api_urls,
    "glossary_terms": glossary_terms
}