# ‘Explain Intervention’ (EI) Experiment

Meng et al. (2018) Berkeley Early Learning Lab  
Keywords: Bayesian network; information theory; causal reasoning; probabilistic models of cognition

## Study

Why do kids fall short of normativeinformation-theoretic metrics such as the expected information
gain (EIG)? 

Is this deviation resulted from mixing discriminatory strategies such as maximizing EIG with confirmatory strategies such as the positive test strategy (PTS)?

Thirty-nine 5- to -7-year-olds solved 6 puzzles where they had one opportunity to intervene on a three-node causal system to identify the correct structure from two possibilities. 

<div align="center">
  <img src="https://raw.githubusercontent.com/lizzij/EI/master/eiPuzzles.png" width="500" align="middle">
<\div>
  
### Purpose

To set up and automate the experiment:
* randomize the puzzles according to experiment design
* display the puzzle and interactive animation in the browser, and
* record children's response automatically to a Google spreadsheet.

### Installation

Install google spreadsheets python API to manage spreadsheets with gspread in Python.

```
$ sudo easy_install pip
```

```
$ pip install gspread
```

##  Finding

Children’s intervention choices were better fit by a Bayesian model that incorporated EIG and PTS compared to alternative models that only considered a single strategy or selected interventions at random. 

The paper containing study design and method can be founds [here](http://docs.wixstatic.com/ugd/9f32e5_17b692ec0a54451a98715fba886644d0.pdf).  
