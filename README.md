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

## Links and sources we used

For all the worksheets:

https://positivepsychology.com/express-feelings/#worksheets 

https://www.therapistaid.com/therapy-worksheet/building-happiness-exercises

https://soniamcdonald.com.au/wp-content/uploads/2020/03/Fear_Mastery-1.pdf

https://www.webmd.com/mental-health/signs-of-fear

https://www.therapistaid.com/therapy-worksheet/core-beliefs

https://www.therapistaid.com/therapy-worksheet/gratitude-journal-three-good-things

https://www.betterup.com/blog/what-to-do-when-you-are-sad

https://eymtherapy.com/wp-content/uploads/2018/03/figuring-out-opposites.pdf

https://positive.b-cdn.net/wp-content/uploads/2021/11/Expressing-Anger.pdf

https://www.therapistaid.com/therapy-worksheet/anger-warning-signs



Pretrained AI model:

https://github.com/SannketNikam/Emotion-Detection-in-Text. 


