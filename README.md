# A Unified Robustness Evaluation Framework for Noisy Slot Filling Task
随着大型语言模型（LLM）能力的不断增强，这些高性能模型在广泛的自然语言处理（NLP）任务中取得了最先进的成果。然而，当应用于真实世界的噪声数据时，模型在常用基准数据集上的性能往往无法准确反映其可靠性和稳健性。为了应对这些挑战，我们提出了一个基于槽填充任务的统一鲁棒性评估框架，以系统地评估LLM在不同输入扰动场景中的对话理解能力。

<div align="center"><img src="resources/nlpcc-main.png" height="23%" width="100%" /></div>

## Overview
This is the repository for Noise-LLM . Noise-LLM assess how well various robustness methods of LLMs perform in real-world noisy scenarios

With the increasing capabilities of large language models (LLMs), these high-performance models have achieved state-of-the-art results on a wide range of natural language processing (NLP) tasks. However, the models' performance on commonly-used benchmark datasets often fails to accurately reflect their reliability and robustness when applied to real-world noisy data. 

We propose a unified robustness evaluation framework based on the slot-filling task to systematically evaluate the dialogue understanding capability of LLMs in diverse input perturbation scenarios. Specifically, we construct a input perturbation evaluation dataset, Noise-LLM, which contains five types of single perturbation and four types of mixed perturbation data. 

Furthermore, we utilize a multi-level data augmentation method (character, word, and sentence levels) to construct a candidate data pool, and carefully design two ways of automatic task demonstration construction strategies (instance-level and entity-level) with various prompt templates. Our aim is to assess how well various robustness methods of LLMs perform in real-world noisy scenarios. The experiments have demonstrated that the current open-source LLMs generally achieve limited perturbation robustness performance. 

| Model                                                    |  Clean     | Typos        | Speech       | Paraphrase  | Simplification |Verbose      |Overall      |
| -------------------------------------------------------- | :------:   | :----:       | :------:     | :------:    | :------:       | :------:    | :------:    | 
| NAT                                                      |  96.01     | 67.47        | 85.23        | 87.73       | 87.32          | 85.41        | 87.21        |
| NAT                                                      |  96.04     | 67.54        | 85.16        | 87.42       | 87.33          | 85.29        | 87.27        |
| PSSAT                                                    |  96.42     | 68.34        | 85.65        | 91.54       | 89.73          | 85.82        | 88.16        |
| Text-davinci-003                                         |  43.09     | 34.26        | 39.34        | 38.42       | 40.12          | 37.18        | 38.54        |
| ChatGPT                                                  |  71.43     | 40.65        | 60.00        | 55.56       | 65.54          | 55.56        | 57.21        |
| ChatGPT+Instance level                                   | 68.21(-3.2) | 65.04(+24.3) | 70.56(+10.5) |58.82(+2.2)  | 73.02(+7.4)    |  61.77(+6.2) | 68.34(+11.1) |
| ChatGPT+Entity level                                     | 74.07(+2.6) | 62.18(+21.5) | 55.39(+4.6)  |75.59(+18.9) | 70.96(+5.4)    | 71.75(+16.1) | 71.55(+14.3) |


