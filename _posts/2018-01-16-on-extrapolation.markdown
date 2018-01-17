---
layout: post
title:  "On Extrapolation. Or 'A Little Formalization Goes a Long Way.'"
date:   2018-01-16
categories: essays
tags: economics, statistics, science, RCT
---

When can one extrapolate claims from experiments, or Randomized Control Trials (RCTs)?

This question is an old hobby-horse in Medicine and Social Studies. It has been discussed within Economics by Manski (2008), Angrist & Pischke (2009) and many others. But interest about it surged particularly since Card & Krueger (1994) and the early 2000's with the inception of institutions such as [J-PAL](https://www.povertyactionlab.org) and [IPA](https://www.poverty-action.org/). More recently, Augus Deaton and Nancy Cartwright have provided a [powerful critique](http://www.sciencedirect.com/science/article/pii/S0277953617307359?via%3Dihub) to the usefulness of RCTs (shorter version [here](http://voxeu.org/article/limitations-randomised-controlled-trials)). [Vivalt (2017a)](http://evavivalt.com/wp-content/uploads/How-Much-Can-We-Generalize.pdf) undertakes an effective comparison of experiments in twenty broad areas of Development to assess how they generalize. On a related note, [Vivalt (2017b)](http://evavivalt.com/wp-content/uploads/Learning.pdf) and [Athey & Wager (2017)](https://arxiv.org/abs/1702.02896) study how much a policy maker can learn from experiments, and how to use that information to implement policy under certain constraints.

Nevertheless, the academic debate about extrapolation has always seemed unnecessarily verbose to me. The conceptual framework behind it is in fact simple, and it could provide us a more synthetic way of pinning down the good and the bad about generalizing claims from experiments.

So here goes my blog post attempt on simplifying it.


### Framework

Let $Y$ be an outcome. Let $X$ be the variable of interest. Define $C$ as a vector of _context_ characteristics and $P$ as a vector of _protocol_ characteristics of the particular experiment/observation/measurement.

Think of $C$ as an abstract vector that contains every dimension of the environment. It contains the institutional background, culture, the weather, and any other idiosyncrasies of the context one can imagine. It may also contain logical entailment claims such as "person is short $\implies$ she is bullied". Context $C$ is purposedly broad and, therefore, usually not fully observable. It's too costly or altogether impossible to quantify elements such as cultural traits or the brain states of the people observed in a study.

The vector $P$, moreover, contains descriptors of the research protocol: dimensions of researcher discretion, survey instruments, framing of questions, details of implementation, sampling choices, etc. As with context above, protocol $P$ is also not fully observable. Besides, the dozens of small design decisions involved in any study may subtly impact measurements and interpretations.

Now, we can write the unknown relationship between outcome and other variables as $Y = f(X, C, P)$. Besides, the causal effect of $X$ on $Y$, for specific values of $X$, is \\[ CE = \frac{\partial f(x,C,P)}{\partial x} \quad \text{ or } \quad CE = f(x_{1}, C, P) - f(x_{0}, C, P) \\] depending on whether changes in $X$ are continuous or discrete, respectively.

### Take-aways

An implicit assumption was made but not described. If we hope to learn anything as a _law_, or some _invariant_ relationship between $Y$ and $X$, we must _assume_ a function $f$ exists to begin with. Otherwise each observation/experiment would output us noise. Of course, however, we don't know _a priori_ such $f$ exists.

Moreover, the formulas make the following points explicit.

- **Perfect extrapolation is only guaranteed in setups with $C' = C$ and $P' = P$**.
: No surprises here. If _everything_ about two setups is equal, then the causal effects must be the same too.

- **Causal effects are local**.
: We only learn about $f$ at particular values of $X$, $C$ and $P$. In particular, even for new setups with $C' = C$ and $P' = P$, without further assumptions, we know nothing about $f$ (and by construction about $CE$) at points other than $x$ (or \{$x_{0},x_{1}$\} for the discrete case).

- **Different observed causal effects $CE$ and $CE'$ may be different for multiple reasons**.
: Context $C$ and protocol $P$ are not fully observable. So one can hardly ever know what varying element in them generated the observed differences in causal effects. Were the effects of labor market training different because the two setups have different kinship systems? Or because people have different levels of noncognitive skills? Or something else? We'll likely never fully know.

- **Elements of $C$ and $P$ may be irrelevant for the causal effects**.
: Most of them probably are indeed irrelevant. My great-grand-parents marriage date has hardly anything to do with my choices of toothpaste. Formally this is saying that some second derivatives of $f$, with respect to $x$ and then to elements of $C$ or $P$, are zero.

- **This discussion is only about identification. Inference is a whole different problem**.
: We haven't touched on sampling, instrumental variables, identifying variation, Local Average Treatment Effects (LATE), etc.
