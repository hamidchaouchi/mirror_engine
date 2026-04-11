import main_engine
import sys

print("\033[1;36m--- Mirror-LLM-v1: Sovereign Intelligence ---\033[0m")
print("\033[1;33mNode: Khemis-Miliana-Alpha [ONLINE]\033[0m")

def chat():
    while True:
        sys.stdout.write("\033[1;32mYou:\033[0m ")
        sys.stdout.flush()
        query = sys.stdin.readline().strip()
        if not query: continue
        if query.lower() in ['exit', 'quit', 'خروج']: break
        
        response = main_engine.process(query)
        print(f"\033[1;34mMirror-LLM:\033[0m {response}")

if __name__ == "__main__":
    chat()
