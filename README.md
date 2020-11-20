# SentiArt
A simple vector space model based tool for sentiment analysis of literary texts.
Detailed information on: https://www.frontiersin.org/articles/10.3389/frobt.2019.00053/full and: https://www.frontiersin.org/articles/10.3389/fpsyg.2020.574746/full

## Main Publication and Use
SentiArt was created for non-commercial use only: if you use it please cite:

    Jacobs AM (2019) Sentiment Analysis for Words and Fiction Characters From the Perspective of Computational (Neuro-)Poetics. Front. Robot. AI 6:53. doi:     10.3389/frobt.2019.00053 

## Empirical Validation
SentiArt has been validated with human rating data in several published studies:
    
    Jacobs AM (2017) Quantifying the Beauty of Words: A Neurocognitive Poetics Perspective. Front. Hum. Neurosci. 11:622. doi: 10.3389/fnhum.2017.00622
    Jacobs AM & Kinder A (2019). Computing the Affective-Aesthetic Potential of Literary Texts, Artifical Intelligence, 1:1, 11–27; doi:10.3390/ai1010002 
    Jacobs AM, Herrmann B, Lauer G, Lüdtke J and Schroeder S (2020) Sentiment Analysis of Children and Youth Literature: Is There a Pollyanna Effect? Front. Psychol. 11:574746. doi: 10.3389/fpsyg.2020.574746 
    
## Vector space models / vsm
The VSMs created to compute the SentiArt .xlsx tables are too big to upload on github. They can be obtained by the author via request to: sentiart0@gmail.com.
The German VSM (skipgram, 300d) is based on the sdewac corpus which can be obtained at: https://www.ims.uni-stuttgart.de/forschung/ressourcen/korpora/sdewac/. The English VSM (skipgram, 500d) is based on the Gutenberg English Literary Corpus (cf. https://www.frontiersin.org/articles/10.3389/fdigh.2018.00005/full) which can be obtained via email to the author.
Both VSMs were created using the gensim library:https://github.com/RaRe-Technologies/gensim. 

### License
Copyright (c) 2011-2017 GitHub Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
