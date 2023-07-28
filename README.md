# A Unified Robustness Evaluation Framework for Noisy Slot Filling Task
随着大型语言模型（LLM）能力的不断增强，这些高性能模型在广泛的自然语言处理（NLP）任务中取得了最先进的成果。然而，当应用于真实世界的噪声数据时，模型在常用基准数据集上的性能往往无法准确反映其可靠性和稳健性。为了应对这些挑战，我们提出了一个基于空位填充任务的统一鲁棒性评估框架，以系统地评估LLM在不同输入扰动场景中的对话理解能力。

<div align="center"><img src="resources/nlpcc-main.png" height="23%" width="100%" /></div>

## 测评基准
基于RADDLE我们构建了Noise LLM数据集，该数据集包括各种噪声扰动。Typos是由非标准缩写引起的，Speech是由ASR系统的识别和合成错误引起的，Simplification指的是用户使用简洁的词语来表达他们的意图{Verbose则指的是使用多余的词语来表示相同的意图，Paraphrase在使用不同单词或根据语言习惯重述文本的用户中也很常见。
此外，我们利用多层次的数据扩充方法（字符、单词和句子级别）来构建候选数据池，并通过各种提示模板精心设计了两种自动任务演示构建策略（实例级别和实体级别）。我们的目标是评估LLM的各种鲁棒性方法在真实世界的噪声场景中的表现。

| Model                                                    |  Clean     | Typos        | Speech       | Paraphrase  | Simplification |Verbose      |Overall      |
| -------------------------------------------------------- | :------:   | :----:       | :------:     | :------:    | :------:       | :------:    | :------:    | 
| NAT                                                      |  96.01     | 67.47        | 85.23        | 87.73       | 87.32          | 85.41        | 87.21        |
| NAT                                                      |  96.04     | 67.54        | 85.16        | 87.42       | 87.33          | 85.29        | 87.27        |
| PSSAT                                                    |  96.42     | 68.34        | 85.65        | 91.54       | 89.73          | 85.82        | 88.16        |
| Text-davinci-003                                         |  43.09     | 34.26        | 39.34        | 38.42       | 40.12          | 37.18        | 38.54        |
| ChatGPT                                                  |  71.43     | 40.65        | 60.00        | 55.56       | 65.54          | 55.56        | 57.21        |
| ChatGPT+Instance level                                   | 68.21(-3.2) | 65.04(+24.3) | 70.56(+10.5) |58.82(+2.2)  | 73.02(+7.4)    |  61.77(+6.2) | 68.34(+11.1) |
| ChatGPT+Entity level                                     | 74.07(+2.6) | 62.18(+21.5) | 55.39(+4.6)  |75.59(+18.9) | 70.96(+5.4)    | 71.75(+16.1) | 71.55(+14.3) |

## 任务介绍
随着大型语言模型（LLM）能力的不断增强，这些高性能模型在广泛的自然语言处理（NLP）任务中取得了最先进的成果。然而，当应用于真实世界的噪声数据时，模型在常用基准数据集上的性能往往无法准确反映其可靠性和稳健性。为了应对这些挑战，我们提出了一个基于填充任务的统一鲁棒性评估框架，以系统地评估LLM在不同输入扰动场景中的对话理解能力。

## 数据集
#### MultiWOZ
#### attraction:

1.i am looking for a swimming pool to go to in the north .

2.give me information about museums in the west side of town .

3.what is the full address and zipcode of cafe jello gallery ?

4.how about a college in the west ?

5.i need to find a place to go for entertainment .

6.are there any museums in the centre ?

7.i would love to maybe tour a college if i can .

8.i need information on the fitzwilliam museum

9.i am looking for attractions in the town centre

10.i am trying to find the parkside pools .

#### hotel:

1.i am looking for 0 star lodging with free parking included

2.can you please recommend one and book it for 5 nights ?

3.i want to book the el shaddai hotel .

4.i am looking to book it for 4 nights for 5 people starting tuesday .

5.great can you book that for 7 people for 3 nights starting friday ?

6.could you help me find a hotel on the west side with free wifi ?

7.6 people for 4 nights .

8.how about two nights ?

9.four stars please .

10.i would like something in the north and has free wifi and free parking if possible .

#### restaurant:

1.i am looking for a cheap restaurant in the centre of town .

2.i want a restaurant that serves molecular gastronomy food .

3.are there any chinese restaurants ?

4.i am looking for a restaurant serving persian food .

5.can i have an european restaurant instead ?

6.i 'd like to find an expensive place to dine in the south .

7.i would be interested in indian food .

8.i want something in the north part of town with swedish food .

9.are there any italian restaurants in the north part of town ?

10.i am looking for a restaurant that serves mexican food and located in the south part of town .

#### train:

1.i 'd like to find a train that leaves monday and arrives by 19:00 .

2.i need to leave from peterborough .

3.just one please .

4.i would like to leave from stansted airport after 11:45 .

5.i 'd like to depart from stevenage after 19:45 .

6.i 'm looking for a train leaving on tuesday please .

7.actually i need to go to london liverpool street from cabridge .

8.i would like to leave anytime after 20:15 .

9.i am looking for a train going to cambridge .

10.i would like to leave broxbourne on tuesday .
