# -*- coding: utf-8 -*-
import pandas as pd
from numpy import nan
import numpy as np

fn = './chicken_data/bbq.csv'
bbq_table = pd.DataFrame.from_csv(fn, encoding='utf-8', index_col=0, header=0)
bbq_table.sido.unique()
sido_alias = """서울시:서울특별시 동작구:서울특별시 서울:서울특별시 강원:강원도 경기:경기도 충남:충청남도
                충북:충청북도 경남:경상남도 경북:경상북도 전남:전라남도 전북:전라북도
                제주도:제주특별자치도 제주:제주특별자치도 제주시:제주특별자치도 제주특별차지도:제주특별자치도
                창원시:경상남도 밀양시:경상남도 김포시:경기도 부천시:경기도
                세종시:세종특별자치시 세종:세종특별자치시 대전광역시광역시:대전광역시
                대전시:대전광역시 대전:대전광역시 대구시:대구광역시 대구:대구광역시 대구공역시:대구광역시
                인천시:인천광역시 인천:인천광역시 광주시:광주광역시 광주:광주광역시
                울산시:울산광역시 울산:울산광역시 부산시:부산광역시 부산:부산광역시"""
sido_dict = dict(aliasset.split(':') for aliasset in sido_alias.split())
sido_dict
bbq_table.sido = bbq_table.sido.apply(lambda v: sido_dict.get(v, v))
bbq_table.sido.unique()
sido_table = pd.DataFrame.from_csv('district2.csv', encoding='utf-8', index_col=0, header=0)
m = bbq_table.merge(sido_table, on=['sido', 'gungu'], how='outer', suffixes=['','_'], indicator=True)
m_result = m.query('_merge == "left_only"')
m_result[['sido','gungu']]

gungu_alias = """고양시덕양구:고양시 일산동구:고양시
                 강서:강서구 영등포:영등포구 강남:강남구 송파:송파구 동작:동작구 사당동:동작구 관악:관악구
                 부천시오정구:부천시 부천시소사구:부천시 시훙시:시흥시 김포:김포시
                 안산시상록구:안산시 광명시소하로:광명시 원미동:부천시
                 안양시만안구:안양시 안양:안양시 웅진:옹진군 진구:부산진구 옹진구:옹진군
                 양편군:양평군 여주군:여주시 동구신천4동436-7:동구 화성:화성시
                 수원시권선구:수원시 용인시수지구:용인시 용인:용인시
                 의창구:창원시 단장면:밀양시 마산합포구:창원시
                 창원시진해구:창원시 진해시:창원시 마산시:창원시
                 창원시마산합포구:창원시 창원시회원구:창원시 창원시의창구:창원시
                 상주시낙양동:상주시 상주시사벌면:상주시 진해구:창원시 성산구:창원시
                 청주시상당구:청주시 해룡면:순천시
                 성주읍:성주군 의성읍:의성군 강화읍:강화군 웅진군:옹진군
                 구좌읍:제주시 북제주군:제주시 신광로:제주시 용문로:제주시 천수로:제주시
                 군포시금정동79-1:군포시 군포시금정동79-1:군포시
                 세종특별자치시:세종시 조치원읍:세종시 새롬중앙로:세종시 시청대로:세종시
                 한솔동:세종시 도담동:세종시 도움8로:세종시 가름로:세종시
                 나리로:세종시 갈매로:세종시 마음로:세종시 보듬로:세종시
                 소담1로:세종시 호려울로:세종시 달빛로:세종시 보람동:세종시
                 연기면:세종시 연동면:세종시 전의면:세종시 누리로28:세종시
                 금남면:세종시 부강면:세종시 연서면:세종시 장군면:세종시
                 전동면:세종시 당진군:당진시 안산시단원구:안산시 청주시흥덕구:청주시 포항시남구:포항시
                 고양시일산서구:고양시 청주시청원구:청주시 천안시서북구:천안시 천안시동남구:천안시 청원시의창구:창원시
                 창원시성산구:창원시 성남시분당구:성남시 수원시팔달구:수원시 성남시수정구:성남시 용인시처인구:용인시
                 용인시기흥구:용인시 수원시장안구:수원시 전주시덕진구:전주시 누리로:세종시 도움3로:세종시 한누리대로:세종시
                 보듬3로:세종시 마음로151:세종시 성남시중원구:성남시 안양시동안구:안양시 수원시영통구:수원시 전주시완산구:전주시
                 청주시서원구:청주시 고양시일산동구:고양시 부천시원미구:부천시 포항시북구:포항시 창원시마산회원구:창원시 마산회원구:창원시
                 청원군:청주시
            """
gungu_dict= dict(aliasset.split(':') for aliasset in gungu_alias.split())
bbq_table.gungu = bbq_table.gungu.apply(lambda v: gungu_dict.get(v, v))
m = bbq_table.merge(sido_table, on=['sido', 'gungu'], how='outer', suffixes=['','_'], indicator=True)
m_result = m.query('_merge == "left_only"')
m_result[['sido','gungu']]
m.to_csv("./chicken_data/bbq_modify.csv", encoding="utf-8", mode='w', index=True)

fn = './chicken_data/pericana.csv'
pericana_table = pd.DataFrame.from_csv(fn, encoding='utf-8', index_col=0, header=0)
pericana_table.sido.unique()
pericana_table[pericana_table['sido'] == '00']
pericana_table = pericana_table.drop(pericana_table.index[1151])
pericana_table[pericana_table['sido'] == '00']
pericana_table[pericana_table['sido'] == '테스트']
pericana_table = pericana_table.drop(pericana_table.index[787])
pericana_table[pericana_table['sido'] == '테스트']
pericana_table[pericana_table['store'] == '서울지사']
pericana_table = pericana_table.drop(pericana_table.index[512])
pericana_table[pericana_table['store'] == '서울지사']
pericana_table[pericana_table['sido'] == ' ']
pericana_table = pericana_table[pericana_table.sido != ' ']
pericana_table.sido.unique()
m = pericana_table.merge(sido_table, on=['sido', 'gungu'], how='outer', suffixes=['','_'], indicator=True)
m_result = m.query('_merge == "left_only"')
m_result[['sido','gungu']]
pericana_table.gungu = pericana_table.gungu.apply(lambda v: gungu_dict.get(v, v))
m = pericana_table.merge(sido_table, on=['sido', 'gungu'], how='outer', suffixes=['','_'], indicator=True)
m_result = m.query('_merge == "left_only"')
m_result[['sido','gungu']]
m.to_csv("./chicken_data/pericana_modify.csv", encoding="utf-8", mode='w', index=True)


fn = './chicken_data/nene.csv'
nene_table = pd.DataFrame.from_csv(fn, encoding='utf-8', index_col=0, header=0)
nene_table.sido.unique()
nene_table.sido = nene_table.sido.apply(lambda v: sido_dict.get(v, v))
nene_table.sido.unique()
nene_table.loc[329, 'sido'] = '서울특별시'
nene_table.loc[329, 'gungu'] = '구로구'
nene_table.loc[329, 'store_address'] = '서울 구로구 개봉동'
nene_table.sido.unique()
m = nene_table.merge(sido_table, on=['sido', 'gungu'], how='outer', suffixes=['','_'], indicator=True)
m_result = m.query('_merge == "left_only"')
m_result[['sido','gungu']]
nene_table.gungu = nene_table.gungu.apply(lambda v: gungu_dict.get(v, v))
m = nene_table.merge(sido_table, on=['sido', 'gungu'], how='outer', suffixes=['','_'], indicator=True)
m_result = m.query('_merge == "left_only"')
m_result[['sido','gungu']]
m.to_csv("./chicken_data/nene_modify.csv", encoding="utf-8", mode='w', index=True)


fn = './chicken_data/kyochon.csv'
kyochon_table = pd.DataFrame.from_csv(fn, encoding='utf-8', index_col=0, header=0)
kyochon_table.sido.unique()
kyochon_table.sido = kyochon_table.sido.apply(lambda v: sido_dict.get(v, v))
kyochon_table.sido.unique()
m = kyochon_table.merge(sido_table, on=['sido', 'gungu'], how='outer', suffixes=['','_'], indicator=True)
m_result = m.query('_merge == "left_only"')
m_result[['sido','gungu']]
kyochon_table.gungu = kyochon_table.gungu.apply(lambda v: gungu_dict.get(v, v))
m = kyochon_table.merge(sido_table, on=['sido', 'gungu'], how='outer', suffixes=['','_'], indicator=True)
m_result = m.query('_merge == "left_only"')
m_result[['sido','gungu']]
m.to_csv("./chicken_data/kyochon_modify.csv", encoding="utf-8", mode='w', index=True)


fn = './chicken_data/cheogajip.csv'
cheogajip_table = pd.DataFrame.from_csv(fn, encoding='utf-8', index_col=0, header=0)
cheogajip_table.sido.unique()
cheogajip_table.sido = cheogajip_table.sido.apply(lambda v: sido_dict.get(v, v))
cheogajip_table.sido.unique()
m = cheogajip_table.merge(sido_table, on=['sido', 'gungu'], how='outer', suffixes=['','_'], indicator=True)
m_result = m.query('_merge == "left_only"')
m_result[['sido','gungu']]
cheogajip_table.gungu = cheogajip_table.gungu.apply(lambda v: gungu_dict.get(v, v))
m = cheogajip_table.merge(sido_table, on=['sido', 'gungu'], how='outer', suffixes=['','_'], indicator=True)
m_result = m.query('_merge == "left_only"')
m_result[['sido','gungu']]
m.to_csv("./chicken_data/cheogajip_modify.csv", encoding="utf-8", mode='w', index=True)


# (문제1) 굽네치킨 데이터수정 및 저장(./chicken_data/goobne_modify.csv) 코드 작성
fn = './chicken_data/goobne.csv'
goobne_table = pd.DataFrame.from_csv(fn, encoding='utf-8', index_col=0, header=0)
goobne_table.sido.unique()
goobne_table.sido = goobne_table.sido.apply(lambda v: sido_dict.get(v, v))
goobne_table.sido.unique()
m = goobne_table.merge(sido_table, on=['sido', 'gungu'], how='outer', suffixes=['','_'], indicator=True)
m_result = m.query('_merge == "left_only"')
m_result[['sido','gungu']]
goobne_table.gungu = goobne_table.gungu.apply(lambda v: gungu_dict.get(v, v))
m = goobne_table.merge(sido_table, on=['sido', 'gungu'], how='outer', suffixes=['','_'], indicator=True)
m_result = m.query('_merge == "left_only"')
m_result[['sido','gungu']]
# m.to_csv("./chicken_data/goobne_modify.csv", encoding="utf-8", mode='w', index=True)
