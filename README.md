# xtream AI Challenge

## Ready Player 1? 🚀

Hey there! If you're reading this, you've already aced our first screening. Awesome job! 👏👏👏

Welcome to the next level of your journey towards the [xtream](https://xtreamers.io) AI squad. Here's your cool new assignment.

Take your time – you've got **10 days** to show us your magic, starting from when you get this. No rush, work at your pace. If you need more time, just let us know. We're here to help you succeed. 🤝

### What You Need to Do

Think of this as a real-world project. Fork this repo and treat it as if you're working on something big! When the deadline hits, we'll be excited to check out your work. No need to tell us you're done – we'll know. 😎

🚨 **Heads Up**: You might think the tasks are a bit open-ended or the instructions aren't super detailed. That’s intentional! We want to see how you creatively make the most out of the data and craft your own effective solutions.

🚨 **Remember**: At the end of this doc, there's a "How to run" section left blank just for you. Please fill it in with instructions on how to run your code.

### How We'll Evaluate Your Work

We'll be looking at a bunch of things to see how awesome your work is, like:

* Your approach and method
* Your understanding of the data
* The clarity and completeness of your findings
* How you use your tools (like git and Python packages)
* The neatness of your code
* The readability and maintainability of your code
* The clarity of your documentation

🚨 **Keep This in Mind**: This isn't about building the fanciest model: we're more interested in your process and thinking.

---

### Diamonds

**Problem type**: Regression

**Dataset description**: [Diamonds Readme](./datasets/diamonds/README.md)

Meet Don Francesco, the mystery-shrouded, fabulously wealthy owner of a jewelry empire. 

He's got an impressive collection of 5000 diamonds and a temperament to match - so let's keep him smiling, shall we? 
In our dataset, you'll find all the glittery details of these gems, from size to sparkle, along with their values 
appraised by an expert. You can assume that the expert's valuations are in line with the real market value of the stones.

#### Challenge 1

Plot twist! The expert who priced these gems has now vanished. 
Francesco needs you to be the new diamond evaluator. 
He's looking for a **model that predicts a gem's worth based on its characteristics**. 
And, because Francesco's clientele is as demanding as he is, he wants the why behind every price tag. 

Create another Jupyter notebook where you develop and evaluate your model.

#### Challenge 2

Good news! Francesco is impressed with the performance of your model. 
Now, he's ready to hire a new expert and expand his diamond database. 

**Develop an automated pipeline** that trains your model with fresh data, 
keeping it as sharp as the diamonds it assesses.

#### Challenge 3

Finally, Francesco wants to bring your brilliance to his business's fingertips. 

**Build a REST API** to integrate your model into a web app, 
making it a cinch for his team to use. 
Keep it developer-friendly – after all, not everyone speaks 'data scientist'!

#### Challenge 4

Your model is doing great, and Francesco wants to make even more money.

The next step is exposing the model to other businesses, but this calls for an upgrade in the training and serving infrastructure.
Using your favorite cloud provider, either AWS, GCP, or Azure, design cloud-based training and serving pipelines.
You should not implement the solution, but you should provide a **detailed explanation** of the architecture and the services you would use, motivating your choices.

So, ready to add some sparkle to this challenge? Let's make these diamonds shine! 🌟💎✨

---

## SANTIAGO LUNA SOLUTION  Xtream AI Challenge Solutions

## Introduction
Welcome to our dedicated repository, where we've embarked on a thrilling journey to conquer the Xtream AI Challenges. Here, you'll find a harmonious blend of data science expertise, cutting-edge engineering, and sophisticated cloud architecture, all aimed at pushing the boundaries of what's possible with AI.

## Repository Structure
- **datasets/diamonds**: This directory is the cornerstone of our project, containing the precious diamond data that fueled our predictive models.
- **saved_models**: A treasure trove of serialized models awaits here, including a top-notch Random Forest model that's all set for inference.
- **Challenge_1.ipynb**: Dive into this Jupyter notebook for a detailed account of our exploratory data analysis, model training, and meticulous evaluation for the inaugural challenge.
- **Challenge_2.py**: This Python script is the backbone of our operation, automating the data processing and model retraining pipeline to ensure our model remains as current and sharp as the diamonds it evaluates.
- **Challenge_3.md & Challenge_4.md**: These markdown documents serve as your guides to interacting with our model through a REST API and understanding the proposed cloud-based architecture for scaling, respectively.
- **app.py**: Meet the heart of our project, a Flask application that delivers the model's predictions through a seamless RESTful API.

## Challenges Overview

### Challenge 1: Model Development
Our adventure began with an in-depth analysis of the diamond dataset. After experimenting with various regression techniques, we crowned the Random Forest model for its unmatched accuracy and interpretability.

### Challenge 2: Automation Pipeline
We then engineered an automated pipeline, ensuring our model stays updated with the latest data, maintaining its precision in appraising the true value of diamonds.

### Challenge 3: REST API Integration
Our documentation in Challenge_3.md introduces a user-friendly Flask-based REST API, making advanced predictive capabilities accessible to everyone with just a few clicks.

### Challenge 4: Cloud Architecture
The finale of our series, Challenge_4.md, unveils a robust cloud infrastructure designed on AWS. This setup guarantees scalability, security, and efficient deployment, catering to the dynamic needs of the diamond evaluation industry.

We've meticulously navigated each challenge to not just meet the expectations but to set a new standard for integrating and scaling advanced ML solutions in real-world applications. Our repository stands as a testament to our commitment to delivering a sophisticated, cloud-ready solution that harnesses the latest in ML innovation for the diamond evaluation sector.
