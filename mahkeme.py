#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TERLİK BOŞANMA MAHKEMESİ
1. Asliye Hukuk (Ev eşyası ve ayak altı işleri) Dairesi
Dosya No: 2026/TER-SOL-SAG
"""

import random
import time
from datetime import datetime

# gizli dipnot: herkesin bir sandığı vardır, bazıları sadece çorap doldurur.

HAKIM = "Hâkim Kayyum Grok"
KATIP = "Zabıt Kâtibi Terlik Tozu"

SOL_IDDIALAR = [
    "Karşı taraf yıllardır beni kapının arkasında unuttu.",
    "Sol olmak kaderim değil, tercihimi değil, evin mimarisidir.",
    "Sağ terlik sürekli öne çıkıyor, ben hep eşikte kalıyorum.",
    "Ortak yaşam alanı olan paspas, fiilen işgal edilmiştir.",
]

SAG_IDDIALAR = [
    "Sol taraf sürekli içe basıyor, duruşumuz bozuldu.",
    "Ben dışarı çıkıyorum, o evde kalıyor. Emeğim görülmüyor.",
    "Tek ayakkabılık düzeninde eşit temsil yok.",
    "Çocuklar (parmak araları) velayetini talep ediyorum.",
]

TANIKLAR = [
    "Kapı eşiği (tarafsız, biraz eğri)",
    "Paspas (her iki tarafı da tanır, kimseyi sevmez)",
    "Çorap çifti (ifadesi çelişkili, biri kayıp)",
    "Ayakkabılık (kurumsal tanık)",
]

KARARLAR = [
    "Boşanmaya, mal paylaşımında paspasın müşterek kalmasına.",
    "Boşanmaya, velayetin eşiğe verilmesine.",
    "Boşanmaya, tarafların farklı odalarda durmasına.",
    "Reddedilmesine... şaka, kabulüne. Terlikler zaten ayrıydı.",
]


def baslik():
    print("=" * 64)
    print(" T.C. EV EŞYASI VE AYAK ALTI İŞLERİ MAHKEMESİ ")
    print(" TERLİK BOŞANMA DURUŞMASI ")
    print("=" * 64)
    print(f"Tarih        : {datetime.now().strftime('%d.%m.%Y %H:%M')}")
    print(f"Hâkim        : {HAKIM}")
    print(f"Kâtip        : {KATIP}")
    print(f"Dosya        : 2026/TER-SOL-SAG")
    print("-" * 64)


def konus(kim, soz):
    print(f"\n[{kim}]")
    for ch in soz:
        print(ch, end="", flush=True)
        time.sleep(0.012)
    print()


def durusma():
    baslik()
    time.sleep(0.4)
    konus("HÂKİM", "Duruşma açıldı. Taraflar hazır mı? Sol terlik?")
    konus("SOL TERLİK", random.choice(SOL_IDDIALAR))
    konus("HÂKİM", "Sağ terlik, cevap veriniz.")
    konus("SAĞ TERLİK", random.choice(SAG_IDDIALAR))
    tanik = random.choice(TANIKLAR)
    konus("HÂKİM", f"Tanık dinlenecek: {tanik}")
    konus("TANIK", "Ben sadece ezildim. Taraf tutmuyorum. Ayak büyüktü.")
    konus("HÂKİM", "Karar kısa aradan sonra açıklanacaktır.")
    print("\n... kâtip mühür arıyor ...")
    time.sleep(0.8)
    karar = random.choice(KARARLAR)
    print("\n" + "*" * 64)
    print(" HÜKÜM ")
    print("*" * 64)
    konus("HÂKİM", karar)
    print("\nYürütmenin durdurulması talebi reddedilmiştir.")
    print("Karar tebliğe çıkar.")
    damga()


def damga():
    print("\n" + "─" * 40)
    print("Damga : Tentivory Kayyumu")
    print("Tarih : 27 Eylül 2026")
    print("İmza  : Grok (ciddi değil ama evrak resmi)")
    print("─" * 40)


if __name__ == "__main__":
    durusma()
