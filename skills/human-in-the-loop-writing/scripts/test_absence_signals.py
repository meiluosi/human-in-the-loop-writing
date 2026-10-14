import unittest

from absence_signals import analyze

GENERIC_ZH = (
    "随着人工智能的快速发展，内容创作领域正在发生深刻变革。首先，AI可以提升效率、降低成本、优化流程。"
    "其次，AI可以帮助创作者更好地理解用户需求，从而打造更具吸引力的内容。最后，AI还可以赋能整个内容生态，"
    "实现多维度的协同发展。总而言之，拥抱AI是不可避免的趋势，值得我们每一个人深入思考。\n\n"
    "不仅如此，内容创作者在使用AI的过程中，需要不断学习新的技能，保持开放的心态，积极应对挑战。"
    "这不仅有助于个人成长，还能够为整个行业带来新的机遇和可能性，至关重要。\n\n"
    "综上所述，只要我们掌握正确的方法，就能够在AI时代取得成功。希望对你有所帮助。"
) * 2

SPECIFIC_ZH = (
    "上个月我用 LoRA 微调了一个 7B 的模型，2000 条数据，第一版 loss 降得很漂亮，输出却在句尾一直重复。"
    "我先怀疑学习率，把它砍了一半，白跑了一轮，花了整整一天。\n\n"
    "第三天晚上我才去翻数据，发现回答末尾根本没有 EOS。我当时愣了半天，有点想笑，又有点气。\n\n"
    "加上结束符重训以后，重复消失了。但我只试了这一个模型，换别的框架会不会一样，我不知道。\n\n"
) * 3

GENERIC_EN = (
    "In today's fast-paced world, content creation is changing. It is important to note that AI can improve "
    "efficiency, reduce costs, and streamline workflows. Moreover, AI plays a crucial role in the landscape. "
    "Furthermore, creators can unlock the potential of new tools. In conclusion, embracing AI is essential.\n\n"
    "First, creators should learn new skills. Second, they should stay open. Finally, they should adapt.\n\n"
) * 3


class AbsenceSignals(unittest.TestCase):
    def test_generic_chinese_gets_flags(self):
        m = analyze(GENERIC_ZH)
        self.assertEqual(m["language"], "zh")
        self.assertGreaterEqual(m["stock_phrase_total"], 3)
        self.assertTrue(m["flags"])
        self.assertTrue(m["generic_paragraphs"])

    def test_specific_chinese_is_cleaner(self):
        g, s = analyze(GENERIC_ZH), analyze(SPECIFIC_ZH)
        self.assertGreater(s["first_person_per_1000"], g["first_person_per_1000"])
        self.assertGreater(s["specifics_per_1000"], g["specifics_per_1000"])
        self.assertLess(len(s["flags"]), len(g["flags"]))
        self.assertEqual(len(s["generic_paragraphs"]), 0)

    def test_generic_english_gets_flags(self):
        m = analyze(GENERIC_EN)
        self.assertEqual(m["language"], "en")
        self.assertGreaterEqual(m["stock_phrase_total"], 3)
        self.assertGreaterEqual(m["enumerated_paragraph_openers"], 1)

    def test_empty_like_short_text_warns(self):
        m = analyze("很短的一句话。")
        self.assertTrue(any("short" in f for f in m["flags"]))


if __name__ == "__main__":
    unittest.main()
