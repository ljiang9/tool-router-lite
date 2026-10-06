import unittest

from tool_router import route


class TestRouter(unittest.TestCase):
    def test_weather(self):
        self.assertEqual(route("今天北京天气怎么样")["intent"], "weather")

    def test_calculator(self):
        self.assertEqual(route("帮我计算 12 乘以 8")["intent"], "calculator")

    def test_search(self):
        self.assertEqual(route("搜索一下量子计算机是什么")["intent"], "search")

    def test_file(self):
        self.assertEqual(route("帮我保存这个文件到目录")["intent"], "file")

    def test_chat(self):
        self.assertEqual(route("你好 hello")["intent"], "chat")

    def test_confidence_range(self):
        r = route("天气和计算都提到")
        self.assertGreaterEqual(r["confidence"], 0)
        self.assertLessEqual(r["confidence"], 1.0)

    def test_unknown(self):
        r = route("zzzz")
        self.assertEqual(r["intent"], "unknown")
        self.assertEqual(r["confidence"], 0.0)


if __name__ == "__main__":
    unittest.main()
