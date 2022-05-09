# LiveseyLang
Implemenation of very simple translator of Dr. Dr. Livesey languge (from russian and to russian).
This language based on Huffman coding with alphabet - {'А', 'Х'}


![AXAXAXAX](https://github.com/goglom/LiveseyLang/blob/main/Livsey.jpg)

# How to use

```python
>> res = russian_to_livesey("Привет", "мир")
>> print(res)
>> print(livesey_to_russian(*res))

['ХХАААххахаххааахаххххаххх', 'хааахаххаххах']
['Привет', 'мир']
```
