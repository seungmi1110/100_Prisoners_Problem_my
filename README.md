# 100명의 죄인 문제
## 문제 설명
100명의 죄수가 각각 1부터 100까지의 고유 번호가 부여되어 있습니다. 이들은 사형을 면하기 위한 마지막 기회로 특별한 도전에 참여하게 됩니다. 방에는 100개의 서랍이 있으며, 각 서랍 안에는 1부터 100까지의 번호가 적힌 종이 한 장씩 무작위로 넣어져 있습니다. 각 죄수는 임의로 선택한 서랍부터 시작하여 자신의 번호가 적힌 종이를 찾아야 합니다. 죄수는 최대 50개의 서랍을 열어볼 수 있으며, 그 이상 열 경우 그 죄수는 실패한 것으로 간주됩니다. 모든 죄수가 자신의 번호를 찾으면 그들은 사형을 면할 수 있습니다. 하나라도 실패하면 모두 사형에 처해집니다.

## 규칙
각 죄수는 순서대로 방에 들어가서 서랍을 엽니다.
죄수는 서랍을 최대 50개까지만 열 수 있습니다.
죄수는 시작하는 서랍을 자유롭게 선택할 수 있으나, 한 번 열기 시작한 서랍의 순서는 변경할 수 없습니다.
목표
모든 죄수가 자신의 번호를 찾아 사형을 면하는 전략을 개발합니다.

## 전략
가장 유명한 전략은 '순환 참조' 전략입니다. 각 죄수는 자신의 번호가 적힌 서랍을 첫 번째로 열고, 그 서랍 안의 숫자를 다음 서랍 번호로 사용하여 이 과정을 반복합니다. 이 전략은 서랍의 배열이 순환 구조를 이루는 경우 최대 50개의 서랍 이내에서 자신의 번호를 찾을 확률을 높여줍니다.

## 구현
이 문제의 구현은 프로그래밍을 통해 시뮬레이션할 수 있습니다. 프로그램은 100개의 서랍에 번호를 무작위로 배치하고, 각 죄수가 순환 참조 전략을 사용하여 자신의 번호를 찾을 수 있는지 검증합니다.


