import yaml
from src.loader import load_model

def test_inference():
    # Загружаем модель
    llm = load_model("config/writer_config.yaml")
    
    # Минимальный промпт
    system = "You are a helpful assistant."
    user = "What is the capital of France? Answer in one word."
    
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": user}
    ]
    
    # Короткий inference
    output = llm.create_chat_completion(
        messages=messages,
        max_tokens=64,
        temperature=0.0,
        top_p=0.9
    )
    
    # Проверка ответа
    if not output or "choices" not in output or not output["choices"]:
        raise ValueError("Model returned empty response")
    
    raw_output = output['choices'][0]['message']['content']
    print(f"RESPONSE: {raw_output}")
    
    return raw_output

if __name__ == "__main__":
    test_inference()
