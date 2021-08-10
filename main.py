from flask import Flask, jsonify
from math import *
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/prime_sieve/<int:n>")
def checkPrime(n):
    numbers = list(range(2,n+1))
    for i in range(2,int(n**0.5)+1):
        for j in range(i*i, n+1, i):
            if j in numbers:
                numbers.remove(j)
    return jsonify(numbers)
#n = int(input("Enter the range to check for prime "))
#prime = checkPrime(n)
#print(f"Prime numbers between 1 to {n} are : ")
#print(*prime)

if __name__ == "__main__":
    app.run(debug=True)
