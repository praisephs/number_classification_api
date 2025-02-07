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

# @app.get("/api/classify-number")
# def classify_number(number: str = Query(..., description="An integer to classify")):
#     """API endpoint to classify a number and return its properties."""

    
#     # Manually Validate Input
#     if not number.lstrip("-").isdigit():
#         return JSONResponse(
#             content={"number": number, "error": True},
#             status_code=400
#         )
#     number = int(number)  # Convert valid input to an integer

#     result = {
#         "number": number,
#         "is_prime": is_prime(number),
#         "is_perfect": is_perfect(number),
#         "properties": get_properties(number),
#         "digit_sum": sum(int(d) for d in str(abs(number))),  # Handle negative numbers
#         "fun_fact": get_fun_fact(number),
#     }

#     return JSONResponse(content=result, media_type="application/json")

# @app.get("/api/classify-number")
# def classify_number(number: str = Query(..., description="A number to classify")):
#     """API endpoint to classify a number and return its properties."""

#     try:
#         number = float(number)  # Convert input to float
#     except ValueError:
#         return JSONResponse(
#             content={"number": number, "error": "Invalid number format."},
#             status_code=400
#         )

#     result = {
#         "number": number,
#         "is_integer": number.is_integer(),  # True if it's a whole number
#         "properties": get_properties(int(number)) if number.is_integer() else ["decimal number"],
#         "digit_sum": sum(int(d) for d in str(abs(int(number)))),  # Sum of digits for whole numbers
#         "fun_fact": get_fun_fact(int(number)) if number.is_integer() else f"{number} is a decimal number.",
#     }

#     # Only check for prime and perfect numbers if it's an integer
#     if number.is_integer():
#         result.update({
#             "is_prime": is_prime(int(number)),
#             "is_perfect": is_perfect(int(number))
#         })
#     else:
#         result.update({"is_prime": False, "is_perfect": False})

#     return JSONResponse(content=result, media_type="application/json")


@app.get("/api/classify-number")
def classify_number(number: str = Query(..., description="A number to classify")):
    """API endpoint to classify a number and return its properties."""

    try:
        number = float(number)  # Convert input to float
    except ValueError:
        return JSONResponse(
            content={"number": number, "error": "Invalid number format."},
            status_code=400
        )

    result = {
        "number": number,
        "is_integer": number.is_integer(),
        "properties": get_properties(int(number)) if number.is_integer() else ["decimal number"],
        "digit_sum": sum(int(d) for d in str(abs(int(number)))) if number.is_integer() else None,
        "fun_fact": get_fun_fact(int(number)) if number.is_integer() else f"{number} is a decimal number.",
    }

    if number.is_integer():
        result.update({
            "is_prime": is_prime(int(number)),
            "is_perfect": is_perfect(int(number))
        })
    else:
        result.update({"is_prime": False, "is_perfect": False})

    return JSONResponse(content=result, media_type="application/json")



@app.get("/")
def health_check():
    """Health check endpoint."""
    return JSONResponse(content={"message": "API is running"}, media_type="application/json")
