from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import math
from fastapi.responses import JSONResponse

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    """Check if a number is a perfect number (sum of proper divisors equals the number)."""
    if n < 2:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def get_properties(n: int):
    """Determine number properties."""
    properties = []
    if is_armstrong(n):
        properties.append("armstrong")
    if n % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    return properties

def get_fun_fact(n: int) -> str:
    """Generate a fun fact based on the number."""
    if is_armstrong(n):
        return f"{n} is an Armstrong number because " + " + ".join(f"{d}^{len(str(n))}" for d in str(n)) + f" = {n}"
    elif is_prime(n):
        return f"{n} is a prime number, meaning it is only divisible by 1 and itself."
    elif is_perfect(n):
        return f"{n} is a perfect number because the sum of its proper divisors equals {n}."
    return f"{n} is an interesting number with unique properties!"



from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import math
from fastapi.responses import JSONResponse

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    """Check if a number is a perfect number."""
    if n < 2:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(abs(int(n)))]  # Ensure we handle negative numbers
    return sum(d ** len(digits) for d in digits) == abs(int(n))

def get_properties(n: float):
    """Determine number properties."""
    properties = []
    
    if n.is_integer():  # Check if it's a whole number
        n = int(n)  # Convert to integer for classification
        if is_armstrong(n):
            properties.append("armstrong")
        if n % 2 == 0:
            properties.append("even")
        else:
            properties.append("odd")
    else:
        properties.append("decimal number")  # Floating point numbers aren't even/odd

    return properties

def get_fun_fact(n: float) -> str:
    """Generate a fun fact based on the number."""
    if not n.is_integer():
        return f"{n} is a decimal number."

    n = int(n)  # Convert to integer for classification
    if is_armstrong(n):
        return f"{n} is an Armstrong number because " + " + ".join(f"{d}^{len(str(n))}" for d in str(n)) + f" = {n}"
    elif is_prime(n):
        return f"{n} is a prime number, meaning it is only divisible by 1 and itself."
    elif is_perfect(n):
        return f"{n} is a perfect number because the sum of its proper divisors equals {n}."
    return f"{n} is an interesting number with unique properties!"


from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import math
from fastapi.responses import JSONResponse

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    """Check if a number is a perfect number."""
    if n < 2:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(abs(n))]  # Ensure we handle negative numbers
    return sum(d ** len(digits) for d in digits) == abs(n)

def get_properties(n: float):
    """Determine number properties."""
    properties = []

    if n.is_integer():  # Check if it's a whole number
        n = int(n)  # Convert to integer for classification
        if is_armstrong(n):
            properties.append("armstrong")
        if n % 2 == 0:
            properties.append("even")
        else:
            properties.append("odd")
    else:
        properties.append("decimal number")  # Floating point numbers aren't even/odd

    return properties

def get_fun_fact(n: float) -> str:
    """Generate a fun fact based on the number."""
    if not n.is_integer():
        return f"{n} is a decimal number."

    n = int(n)  # Convert to integer for classification
    if is_armstrong(n):
        return f"{n} is an Armstrong number because " + " + ".join(f"{d}^{len(str(n))}" for d in str(n)) + f" = {n}"
    elif is_prime(n):
        return f"{n} is a prime number, meaning it is only divisible by 1 and itself."
    elif is_perfect(n):
        return f"{n} is a perfect number because the sum of its proper divisors equals {n}."
    return f"{n} is an interesting number with unique properties!"

@app.get("/api/classify-number", response_class=JSONResponse)
async def classify_number(number: str = Query(..., description="A number to classify")):
    """API endpoint to classify a number and return its properties."""

    # Validate the number input
    try:
        number = float(number)  # Convert input to float (handles integers too)
    except ValueError:
        return JSONResponse(
            status_code=400,
            content={"number": number, "error": "Invalid input. Only numbers are allowed."}
        )
        

    result = {
        "number": number,
        "is_integer": number.is_integer(),
        "is_prime": is_prime(int(number)) if number.is_integer() else False,
        "is_perfect": is_perfect(int(number)) if number.is_integer() else False,
        "properties": get_properties(number),
        "digit_sum": sum(int(d) for d in str(abs(int(number)))) if number.is_integer() else None,
        "fun_fact": get_fun_fact(number),
    }

    return JSONResponse(content=result, media_type="application/json")


@app.get("/")
def health_check():
    """Health check endpoint."""
    return JSONResponse(content={"message": "API is running"}, media_type="application/json")
