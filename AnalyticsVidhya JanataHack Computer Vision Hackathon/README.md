## About
Computer Vision as a field of research is notoriously difficult. Almost no research problem has been satisfactorily solved. One main reason for this difficulty is that the human visual system is simply too good for many tasks (e.g., face recognition), so that computer vision systems suffer by comparison. 

A human can recognize faces under all kinds of variations in illumination, viewpoint, expression, etc. In most cases we have no difficulty in recognizing a friend in a photograph taken many years ago. Also, there appears to be no limit on how many faces we can store in our brains for future recognition. There appears no hope in building an autonomous system with such stellar performance.

Given all this, computer vision has shown a lot of promise and reshaping the future of various industries such as automobile industry, healthcare industry, financial industry and so on

This weekend we bring to you another hackathon to apply your deep learning skills to solve a computer vision problem. This time you are in for a two week ride so brush up on our computer vision skills and hop on.

## Emergency vs Non-Emergency Vehicle Classification
Fatalities due to traffic delays of emergency vehicles such as ambulance & fire brigade is a huge problem. In daily life, we often see that emergency vehicles face difficulty in passing through traffic. So differentiating a vehicle into an emergency and non emergency category can be an important component in traffic monitoring as well as self drive car systems as reaching on time to their destination is critical for these services.

In this problem, you will be working on classifying vehicle images as either belonging to the emergency vehicle or non-emergency vehicle category. For the same, you are provided with the train and the test dataset. Emergency vehicles usually includes police cars, ambulance and fire brigades.

## Data Description
train.zip: contains 2 csvs and 1 folder containing image data
train.csv – [‘image_names’, ‘emergency_or_not’] contains the image name and correct class for 1646 (70%) train images
images – contains 2352 images for both train and test sets
test.csv: [‘image_names’] contains just the image names for the 706 (30%) test images
sample_submission.csv: [‘image_names’,’emergency_or_not­’] contains the exact format for a valid submission (1 - For Emergency Vehicle, 0 - For Non Emergency Vehicle)

## LeaderBoard
### Private LB : 0.9760765550 (Rank 30)
### Public LB: 0.9756944444 (Rank 43)
[https://datahack.analyticsvidhya.com/contest/janatahack-computer-vision-hackathon/#LeaderBoard]
