from identifier import detect

tests = [
    ("The weather is very nice today", "English"),
    ("I am going to the market to buy vegetables", "English"),
    ("नमस्ते, आप कैसे हैं?", "Hindi"),
    ("मुझे आज बाजार जाना है", "Hindi"),
    ("నమస్కారం, మీరు ఎలా ఉన్నారు?", "Telugu"),
    ("నేను ఈ రోజు మార్కెట్‌కి వెళ్తున్నాను", "Telugu"),
    ("Hoy hace muy buen tiempo en la ciudad", "Spanish"),
    ("Voy al mercado a comprar verduras", "Spanish"),
    ("Aujourd'hui il fait très beau dans la ville", "French"),
    ("Je vais au marché pour acheter des légumes", "French"),
    ("I love eating mangoes in summers","English"),
    ("hello","English"),
    ("gracias","Spanish"),
    ("आज मौसम सुहावना है","Hindi"),
    ("El tiempo está agradable hoy","Spanish"),
    ("ఈరోజు వాతావరణం ఆహ్లాదకరంగా ఉంది","Telugu"),
    ("hi", "English"),
    ("ok thanks", "English"),
    ("hola", "Spanish"),
    ("merci beaucoup", "French"),
    ("bonjour", "French"),
    ("muchas gracias amigo", "Spanish"),
    ("I will meet you at the station", "English"),
    ("Nos vemos mañana en la estación", "Spanish"),
    ("On se retrouve demain à la gare", "French"),
    ("namaste", "Hindi")
]

correct = 0
for text, truth in tests:
    guess = detect(text)
    ok = (guess == truth)
    correct += ok
    print("OK  " if ok else "FAIL", truth, "->", guess, "|", text)

print()
print("Accuracy:", correct, "/", len(tests))