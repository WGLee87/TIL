{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###### 데이터베이스 모델링 (Database Modeling)\n",
    "\n",
    "데이터베이스 모델링(또는 데이터 모델링)이란 현실 세계에서 사용되는 작업이나 사물들을 DBMS의 데이터베이스 개체로 옮기기 위한 과정이라고 할 수 있습니다.\n",
    "\n",
    "데이터베이스 모델링은 모델링을 하는 사람이 어떤 사람이냐에 따라서 각기 다른 결과가 나올 수밖에 없고 '많은 실무 경험과 지식을 가진 사람이 더 좋은 모델링을 한다' 라고 합니다.\n",
    "\n",
    "3가지의 모델링 방식이 있다.\n",
    "    - 개념적 모델링\n",
    "    - 논리적 모델링\n",
    "    - 물리적 모델링\n",
    "\n",
    "개념적 모델링은 주로 업무 분석 단계에서 진행되며 논리적 모델링은 업무 분석의 후반부와 시스템 설계를 하는 부분에 걸쳐서 진행된다고 할 수 있습니다. 마지막으로 물리적 모델링은 시스템 설계 단계의 후반부에서 주로 진행됩니다.\n",
    "\n",
    "그러나 모두 절대적인 것은 아니며 사람에 따라 조금씩 차이를 보이기도 합니다."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "워크벤치는 이 모델링 툴을 제공해주는데 그것이 바로 ERD툴입니다.\n",
    "\n",
    "###### ERD란?\n",
    "Entity Relationship Diagram의 약자로, 개체관계도라고 부릅니다\n",
    "\n",
    "###### 장점\n",
    "1. 만들고자 하는 바를 더 명확하게 알 수 있다.\n",
    "2. 이해하고 소통하기에 편리하다.\n",
    "3. RDBMS 데이터 설계가 쉬워진다.\n",
    "\n",
    "###### 데이터베이스\n",
    "모델링에서는 데이터베이스를 Schema라고 부릅니다.\n",
    "\n",
    "실습을 해보기 전에 ERD에 대해 소개를 하였습니다. 실습은 워크벤치를 사용하였고. MySQL workbench는 약 10년 정도 상업용으로 개발되어 판매되다가, MySQL에서 workbench를 인수하여 오픈소스로 풀었다고 합니다."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###### 실습과정"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. FILE > New Model 클릭\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. Model의 이름 설정(안해도 됨)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3. 테이블 생성 > 흰 바탕에 클릭 > 컬럼 생성\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4. PK와 FK 설정 (설정 시 place a relationship using existing columns 선택 > 자식테이블의 해당 컬럼 열을 먼저 클릭 후 부모테이블의 컬럼 열 클릭)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5. 관계 생성\n",
    "6. 저장 > database의 forward engineer 선택 > continue \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "최종적으로 모델링이 되어 있는 db와 table 생성"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
