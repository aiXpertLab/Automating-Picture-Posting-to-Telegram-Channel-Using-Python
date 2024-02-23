## Auto Post Pictures to Telegram from Picture Pool with Sweet Caption

The app will randomly pick a picture from Picture Pool, post to Telegram Group, and move the picture to the Destination. The caption will be randomly chosen from Caption.txt.

change `source="E:/gDrive/38.Pic/Tele"` to the appropriate picture pool.

change `dest  ="E:/gDrive/38.Pic/Tele/web"` to the destination you want to drop your picture.

Open `captions.txt` and put down the captions you like. Will be caught by line. 


```
pip install shutil
pip install telebot
pip install dotenv
```

> [!NOTE] 

>Bonus: 
>
>Batch Convert WEBP to JPG
Copy BatchConvertWEBP2JPG.py to the target folder. 

```python3 BatchConvertWEBP2JPG.py ```

Convert all the pictures in WEBP to JPG.
