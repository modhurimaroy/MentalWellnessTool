# MentalWellnessTool

## Purpose of the project

This project was made for the Hack This Fall Virtual Hackathon. In it, we are creating a simple tool that allows a user to journal their feelings. The app responds to the entry with what emotion the user is experiencing as well as recommendations, and works through a worksheet that you would find assigned by a therapist. In our research, we found the following article that included a worksheet: https://positivepsychology.com/express-feelings/#worksheets

As a result of the limited time, we chose to use the model in the following github repo: https://github.com/SannketNikam/Emotion-Detection-in-Text. Existing APIs for sentiment analysis give outputs that are too vague, as they only categorize text as 'negative', 'neutral', or 'positive'. We felt it would be more useful if the user was more informed on what possible emotion that is. 

## How to use

First, clone the repo. Then do the following:

1. navigate to the repo folder

2. install the required modules

```pip install -r reqs```

3. run the program

On windows:

```python .\gui.py```

On mac:

```python3 gui.py```


Note:

main.py was used for proof of concept and quick prototyping. The final version of the project is gui.py which is mostly frontend and backend.py which is imported into gui.py

## Limitations and future

Due to the time constraints we weren't able to train our own model. Instead we used the model linked earlier, which unfortunately is not as accurate as we would like. However, since sentiment analysis is to vague, it felt more fitting to use a pre-trained model that we can switch out with our own model down the line. Additionally, the software robustness could be improved. 

However, for a project essentially completed in under 24hrs due to timezone differences, we believe it showcases the main intent and vision of the project.




