# Python-Primesplot
This is a code I found in [this reddit post](https://www.reddit.com/r/askscience/comments/5bqlss/why_prime_numbers_and_only_them_afaik_are_giving/) and It's results were interesting. It produces 
points
```
    (cos(p) , sin(p+gap(p)))
```
where gap(p) gives you the difference between p and the next prime as it says in comments.
<br>
Read comments for additional info. The result would something like:
<p align="center">
    <img src="result.png" width="600">
</p>

# Usage
```
    pip install -r requirements.txt
    python script.py 7000000 (integer for number of times of running)
```
