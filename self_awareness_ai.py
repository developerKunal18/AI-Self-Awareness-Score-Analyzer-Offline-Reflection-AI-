print("🧠 AI Self-Awareness Score Analyzer \n")

reflection = int(input("Reflection quality (1–5): "))
emotion = int(input("Emotional awareness (1–5): "))
learning = int(input("Learning from mistakes (1–5): "))
planning = int(input("Planning for improvement (1–5): "))

score = (
    (reflection + emotion + learning + planning) / 20
) * 100

print("\n📊 SELF-AWARENESS REPORT")
print(f"Self-Awareness Score: {score:.1f} / 100")

print("\n🧭 AI Assessment")

if score >= 80:
    print("🌟 High self-awareness. Excellent personal insight!")
elif score >= 60:
    print("🙂 Moderate self-awareness. Keep reflecting.")
elif score >= 40:
    print("⚠️ Low self-awareness. Reflection needs improvement.")
else:
    print("🚨 Very low self-awareness. Immediate self-reflection needed.")

print("\n🧭 AI Reflection Tips")

if reflection < 3:
    print("• Spend time journaling daily")
if emotion < 3:
    print("• Practice identifying emotions clearly")
if learning < 3:
    print("• Review mistakes and lessons learned")
if planning < 3:
    print("• Set small improvement goals")
