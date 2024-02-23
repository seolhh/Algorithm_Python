-- 코드를 입력하세요
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
WHERE ADDRESS LIKE "강원도%"  # 조건이 어떤 특정 단어 ~를 포함하고 있는거라면 like사용, 뒤에 오는 애들이 더 있으면 % 붙이기
ORDER BY FACTORY_ID