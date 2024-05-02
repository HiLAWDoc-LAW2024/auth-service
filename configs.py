from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from supabase import create_client, Client


# JWT configs
SECRET_KEY = "nh124WYqX+Fpnyc61sXQz95v6DLm07MAwFM8uPwVihu57XmxK4/DOPG3lMT5bJfN"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120

# DB configs
SUPABASE_URL = "https://mnxfqoncylcvkflmreee.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1ueGZxb25jeWxjdmtmbG1yZWVlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTQ2MzE3NzYsImV4cCI6MjAzMDIwNzc3Nn0.duoETYSK3wjAAxY73-mw2uUFH8UXyzrIYwyg2x01z5k"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
