franchise = ['비비큐', 'bhc','페리카나', '네네치킨', '교촌', '처갓집','굽네', '호식이', '멕시카나', '또래오래', '또봉이통닭', '지코바', '노랑통닭', '썬더치킨', '맥시칸치킨', '부어치킨', '치킨마루','땅땅치킨','훌랄라치킨', '티바두마리', '신통치킨', '치킨플러스', '60계', '돈치킨','투존치킨', '깐부치킨', '깻잎두마리', '디디치킨', '치킨매니아', '호치킨', '오꾸닭', '충만치킨', '푸라닭']

franchise_dict = {}
for i in franchise:
    franchise_dict[i] = []
for j in franchise:
    for x in wording:
        if j in x:
            franchise_dict[j].append(x)

for i in franchise_dict:
    if franchise_dict[i] == None:
        del franchise_dict[i]

franchise_num = {}
for i in franchise_dict:
    franchise_num[i] = len(franchise_dict[i])
franchise_num = sorted(franchise_num.items(),key=(lambda x: x[1]),reverse = True)

from chatspace import ChatSpace
spacer = ChatSpace()
for name in franchise_dict:
    franchise_dict[name] = spacer.space(franchise_dict[name])



franchise_keyword = {}
for i in franchise_dict:
    franchise_keyword[i] = []
    
josa = ['하다','이다','있다'] 
stopwords = ['아', '휴', '아이구', '아이쿠', '아이고', '어', '나', '우리', '저희', '따라', '의해', '을', '를', '에','없다', '의', '가', '으로', '너무','좋다', '로', '주다','에게', '뿐이다', '의거하여', '근거하여', '입각하여', '기준으로', '예하면', '예를 들면', '예를 들자면', '저', '소인', '소생', '저희', '지말고', '하지마', '하지마라', '다른', '물론', '또한', '그리고', '비길수 없다', '해서는 안된다', '뿐만 아니라', '만이 아니다', '만은 아니다', '막론하고', '관계없이', '그치지 않다', '그러나', '그런데', '하지만', '든간에', '논하지 않다', '따지지 않다', '설사', '비록', '더라도', '아니면', '만 못하다', '하는 편이 낫다', '불문하고', '향하여', '향해서', '향하다', '쪽으로', '틈타', '이용하여', '타다', '오르다', '제외하고', '이 외에', '이 밖에', '하여야', '비로소', '한다면 몰라도', '외에도', '이곳', '여기', '부터', '기점으로', '따라서', '할 생각이다', '하려고하다', '이리하여', '그리하여', '그렇게 함으로써', '하지만', '일때', '할때', '앞에서', '중에서', '보는데서', '으로써', '로써', '까지', '해야한다', '일것이다', '반드시', '할줄알다', '할수있다', '할수있어', '임에 틀림없다', '한다면', '등', '등등', '제', '겨우', '단지', '다만', '할뿐', '딩동', '댕그', '대해서', '대하여', '대하면', '훨씬', '얼마나', '얼마만큼', '얼마큼', '남짓', '여', '얼마간', '약간', '다소', '좀', '조금', '다수', '몇', '얼마', '지만', '하물며', '또한', '그러나', '그렇지만', '하지만', '이외에도', '대해 말하자면', '뿐이다', '다음에', '반대로', '반대로 말하자면', '이와 반대로', '바꾸어서 말하면', '바꾸어서 한다면', '만약', '그렇지않으면', '까악', '툭', '딱', '삐걱거리다', '보드득', '비걱거리다', '꽈당', '응당', '해야한다', '에 가서', '각', '각각', '여러분', '각종', '각자', '제각기', '하도록하다', '와', '과', '그러므로', '그래서', '고로', '한 까닭에', '하기 때문에', '거니와', '이지만', '대하여', '관하여', '관한', '과연', '실로', '아니나다를가', '생각한대로', '진짜로', '한적이있다', '하곤하였다', '하', '하하', '허허', '아하', '거바', '와', '오', '왜', '어째서', '무엇때문에', '어찌', '하겠는가', '무슨', '어디', '어느곳', '더군다나', '하물며', '더욱이는', '어느때', '언제', '야', '이봐', '어이', '여보시오', '흐흐', '흥', '휴', '헉헉', '헐떡헐떡', '영차', '여차', '어기여차', '끙끙', '아야', '앗', '아야', '콸콸', '졸졸', '좍좍', '뚝뚝', '주룩주룩', '솨', '우르르', '그래도', '또', '그리고', '바꾸어말하면', '바꾸어말하자면', '혹은', '혹시', '답다', '및', '그에 따르는', '때가 되어', '즉', '지든지', '설령', '가령', '하더라도', '할지라도', '일지라도', '지든지', '몇', '거의', '하마터면', '인젠', '이젠', '된바에야', '된이상', '만큼', '어찌됏든', '그위에', '게다가', '점에서 보아', '비추어 보아', '고려하면', '하게될것이다', '일것이다', '비교적', '좀', '보다더', '비하면', '시키다', '하게하다', '할만하다', '의해서', '연이서', '이어서', '잇따라', '뒤따라', '뒤이어', '결국', '의지하여', '기대여', '통하여', '자마자', '더욱더', '불구하고', '얼마든지', '마음대로', '주저하지 않고', '곧', '즉시', '바로', '당장', '하자마자', '밖에 안된다', '하면된다', '그래', '그렇지', '요컨대', '다시 말하자면', '바꿔 말하면', '즉', '구체적으로', '말하자면', '시작하여', '시초에', '이상', '허', '헉', '허걱', '바와같이', '해도좋다', '해도된다', '게다가', '더구나', '하물며', '와르르', '팍', '퍽', '펄렁', '동안', '이래', '하고있었다', '이었다', '에서', '로부터', '까지', '예하면', '했어요', '해요', '함께', '같이', '더불어', '마저', '마저도', '양자', '모두', '습니다', '가까스로', '하려고하다', '즈음하여', '다른', '다른 방면으로', '해봐요', '습니까', '했어요', '말할것도 없고', '무릎쓰고', '개의치않고', '하는것만 못하다', '하는것이 낫다', '매', '매번', '들', '모', '어느것', '어느', '로써', '갖고말하자면', '어디', '어느쪽', '어느것', '어느해', '어느 년도', '라 해도', '언젠가', '어떤것', '어느것', '저기', '저쪽', '저것', '그때', '그럼', '그러면', '요만한걸', '그래', '그때', '저것만큼', '그저', '이르기까지', '할 줄 안다', '할 힘이 있다', '너', '너희', '당신', '어찌', '설마', '차라리', '할지언정', '할지라도', '할망정', '할지언정', '구토하다', '게우다', '토하다', '메쓰겁다', '옆사람', '퉤', '쳇', '의거하여', '근거하여', '의해', '따라', '힘입어', '그', '다음', '버금', '두번째로', '기타', '첫번째로', '나머지는', '그중에서', '견지에서', '형식으로 쓰여', '입장에서', '위해서', '단지', '의해되다', '하도록시키다', '뿐만아니라', '반대로', '전후', '전자', '앞의것', '잠시', '잠깐', '하면서', '그렇지만', '다음에', '그러한즉', '그런즉', '남들', '아무거나', '어찌하든지', '같다', '비슷하다', '예컨대', '이럴정도로', '어떻게', '만약', '만일', '위에서 서술한바와같이', '인 듯하다', '하지 않는다면', '만약에', '무엇', '무슨', '어느', '어떤', '아래윗', '조차', '한데', '그럼에도 불구하고', '여전히', '심지어', '까지도', '조차도', '하지 않도록', '않기 위하여', '때', '시각', '무렵', '시간', '동안', '어때', '어떠한', '하여금', '네', '예', '우선', '누구', '누가 알겠는가', '아무도', '줄은모른다', '줄은 몰랏다', '하는 김에', '겸사겸사', '하는바', '그런 까닭에', '한 이유는', '그러니', '그러니까', '때문에', '그', '너희', '그들', '너희들', '타인', '것', '것들', '너', '위하여', '공동으로', '동시에', '하기 위하여', '어찌하여', '무엇때문에', '붕붕', '윙윙', '나', '우리', '엉엉', '휘익', '윙윙', '오호', '아하', '어쨋든', '만 못하다', '하기보다는', '차라리', '하는 편이 낫다', '흐흐', '놀라다', '상대적으로 말하자면', '마치', '아니라면', '쉿', '그렇지 않으면', '그렇지 않다면', '안 그러면', '아니었다면', '하든지', '아니면', '이라면', '좋아', '알았어', '하는것도', '그만이다', '어쩔수 없다', '하나', '일', '일반적으로', '일단', '한켠으로는', '오자마자', '이렇게되면', '이와같다면', '전부', '한마디', '한항목', '근거로', '하기에', '아울러', '하지 않도록', '않기 위해서', '이르기까지', '되다', '인해', '까닭으로', '이유만으로', '그래서', '이 때문에', '그러므로', '까닭', '있다', '결론을 낼 수 있다', '으로 인하여', '있다', '어떤것', '관계가 있다', '관련이 있다', '연관되다', '어떤것들', '에 대해', '이리하여', '그리하여', '여부', '하기보다는', '하느니', '하면 할수록', '운운', '이러이러하다', '하구나', '하도다', '다시말하면', '다음으로', '에 있다', '에 달려 있다', '우리', '우리들', '오히려', '하기는한데', '어떻게', '어떻해', '어찌됏어', '어때', '어째서', '본대로', '자', '이', '이쪽', '여기', '이것', '이번', '이렇게말하자면', '이런', '이러한', '이와 같은', '요만큼', '요만한 것', '얼마 안 되는 것', '이만큼', '이 정도의', '이렇게 많은 것', '이와 같다', '이때', '이렇구나', '것과 같이', '끼익', '삐걱', '따위', '와 같은 사람들', '부류의 사람들', '왜냐하면', '중의하나', '오직', '오로지', '에 한하다', '하기만 하면', '도착하다', '까지 미치다', '도달하다', '정도에 이르다', '할 지경이다', '결과에 이르다', '관해서는', '여러분', '하고 있다', '한 후', '혼자', '자기', '자기집', '자신', '우에 종합한것과같이', '총적으로 보면', '총적으로 말하면', '총적으로', '대로 하다', '으로서', '참', '그만이다', '할 따름이다', '쿵', '탕탕', '쾅쾅', '둥둥', '봐', '봐라', '아이야', '아니', '와아', '응', '아이', '참나', '년', '월', '일', '령', '영', '일', '이', '삼', '사', '오', '육', '륙', '칠', '팔', '구', '이천육', '이천칠', '이천팔', '이천구', '하나', '둘', '셋', '넷', '다섯', '여섯', '일곱', '여덟', '아홉', '령']
from soylemma import Lemmatizer 
lemmatizer = Lemmatizer() 

for i in franchise_keyword:
    for j in franchise_dict[i]:
        j = j.replace(".","")
        j = j.replace('#','') 
        j = j.replace('치킨','')
        j = j.replace (i,'')
        
        for x in j.split():
            if lemmatizer.lemmatize(x) == []:
                if x not in josa or x not in stopwords:
                    franchise_keyword[i].append(x)
            else:
                a = lemmatizer.lemmatize(x)
                if len(a)>0:
                    for y in range(len(a)):
                        if a[y][1]=='Adjective' or a[y][1]== 'Verb':
                            if a[y][0] not in josa and a[y][0] not in stopwords:
                                franchise_keyword[i].append(a[y][0])
                                break
                    if a[0][0] not in josa and a[0][0] not in stopwords:
                        franchise_keyword[i].append(a[0][0])

from konlpy.tag import*
okt = Okt()

for i in franchise_keyword:
    tags = []
    Filter = []
    for j in franchise_keyword[i]:
        morph = okt.pos(j)
        tags.append(morph)
    for sentence in tags:
        for word,tag in sentence:
            if tag in ['Noun','Adjective','Adverb']:
                Filter.append(word)
    franchise_keyword[i] = Filter

from collections import Counter
franchise_frequent_keyword = {}
for i in franchise_dict:
    franchise_frequent_keyword[i] = []
for i in franchise_keyword:
    counts = Counter(franchise_keyword[i])
    franchise_frequent_keyword[i].append(counts.most_common())

 kyochon = ['신화순살', '신화오리지날','살살치킨', '소이살살','라이스', '허니순살', '허니오리지날', '허니콤보', '허니스틱', '레드순살', '레드오리지날', '레드콤보', '레드스틱', '반반콤보', '반반오리지날', '반반순살', '레허반반순살', '반반스틱', '후라이드', '교촌콤보', '교촌오리지날', '교촌순살', '교촌스틱']

 bbq = ['핫황금올리브크리스피', '레드착착','블랙페퍼', '찐킹소스', '콤보반반', '황금올리브치킨', '황금올리브닭다리', '황금올리브순살', '황금올리브치킨', '바삭칸치킨', '황금올리브치킨속안심', '순살크래커', '황금올리브양념', '시크릿양념치킨', '마라핫치킨', '치즐링', '극한매운왕갈비치킨', '극한왕갈비치킨', '허니버터갈릭스', '소이갈릭스', '써프라이드', '뱀파이어치킨', '자메이카통다리','스모크치킨','매달구']

 bhc= ['블랙올리브', '마라칸', '치하오', '커리퀸', '맵스터', '맛초킹', '뿌링클', '뿌링클HOT', '갈비레오', '붐바스틱', '바삭클', '스윗텐더', '해바라기후라이드', '해바라기핫후라이드', '골드킹', '소떡강정', '소이바베큐순살', '소이바베큐', '매운맛양념치킨', '양념']

 pericana = ['후라이드', '양념', '매운후라이드', '매운양념', '마늘', '파닭', '간장', '핫칠리', '핫데불', '누꼬', '와사비톡', '뿌리오', '맵삭치킨', '두마리치킨']

 nene = ['크리미언', '핫블링', '후라이드', '네네옛날통닭', '양념', '스노윙', '쇼킹핫', '후닭', '소이갈릭', '윙봉후닭', '포테이토짜용', '핫후닭', '파닭', '마늘치킨', '참나무훈제', '골드링양파닭', '구운치킨', '구운양념', '구운쇼킹핫', '베이크양념', '베이크핫양념', '베이크', '후라이드윙봉', '후라이드닭날개']

 cheogatjib = ['후라이드', '허니올리고당야채', '매운불', '핫슈프림', '치즈슈프림', '슈프림골드', '트러플슈프림', '슈프림', '와락', '핫불훈제', '닭강정', '훈제', '파인유자', '골드치즈', '화이트치킨',]

 goobne = ['굽네오리지널', '마라볼케이노', '스윗볼케이노', '볼케이노모짜렐라', '볼케이노쌀떡볶이', '반반D', '그릴후랑크', '볼케이노', '고추바사삭', '허니멜로', '핫갈비천왕', '갈비천왕', '양념', '딥치즈']

 hosik = ['후라이드', '매운양념', '양념', '매우간장', '간장', '땡초불꽃', '불짬뽕', '스윗츠갈릭']

 mexicana = ['까르보불닭', '불닭', '뿌리고', '강정', '땡초', '후라이드', '양념', '반반']

 ddoraeorae = ['고추단짠', '단짠', '콘듀', '볼빨간', '리얼핫영념', '엔젤', '핫양념', '양념', '마왕', '갈릭반핫양념', '어메이찡', '오곡후라이드', '갈리플러스', '스낵후라이드', '맛강정', '목우촌파닭', '라이스볼', '바베큐']

ddobongi = ['또봉이통닭', '양념', '갈비', '간장마늘', '또봉이파닭', '맵닭', '고추', '깐풍', '반반', '윙봉', '또봉이윙봉', '양념똥집', '똥집튀김', '마늘똥집']

 gicova = ['순살소금', '순살양념', '소금', '양념', '뼈있는반반', '순살반반']

 norang = ['알싸한마늘', '큰후라이드', '큰깐풍', '순살3종', '큰양념', '매콤후라이드', '큰반반', '고바치', '간바치', '웰빙파닭', '똥집감자', '깐풍똥집']

 thunder = ['크리스피', '양념', '파닭', '마늘', '순살', '칠리', '어니언', '양파&간장', '간장' , '반반', '옛날통닭']

 mexican = ['후라이드', '양념', '파인애플', '훈제', '갈릭', '소이', '파닭', '어니언', '치즈랑', '매콤', '반반', '반반반']

 chickenmaru = ['크리스피', '눈꽃', '양념', '마늘간장', '파닭', '맛깔난어니언빠사칸', '맛깔난어니언', '레디핫치즈','빠사칸현미', '빠사칸허니', '빠사칸레드', '윙봉현미', '윙봉허니', '윙봉레드', '맛짱똥집후라이드', '로스트', '바베큐로스트', '쌀베이크']

 ddangddang = ['똥집후라이드', '땅땅닭다리', '땅땅두다리', '오왕', '불골드윙', '땅땅소금', '땅땅핫양념', '골드크런치킹', '허브소이', '핫불갈비', '순살후라이드', '순살양념후반', '순살양념', '매콤찹스', '후왕', '불갈비', '서울', '핫홀릭', '허브순살', '땅땅양념']

 tiba = ['크리미양파', '후라이드', '수제아삭킹', '삼삼', '똥집튀김', '오삼', '불양념', '양념', '땡초갈릭' , '마늘간장', '치새떡', '치떡', '커리양념', '치즈스노우퀸', '새떡']

 shintong = ['방통', '통통', '신통', '와사비', '크닭', '양념', '크리스피', '간장', '순살후라이드', '순살양념', '불칸', '어니언', '순살파닭', '소이콤보', '레드콤보']

 chickenplus = ['극장판', '크리미어니언', '양념톡톡', '핫쵸킹톡톡', '꿔바로우톡톡', '눈맞은치킨', '핫쵸킹', '크리스피후라이드', '마늘스태미너', '바삭담백한후라이드', '간장', '토마토커리순살', '개매운', '순살양파', '강정', '양념', '쉑쉑양꼬', '꿔바로우']

chicken60 = ['더매운고추', '크리스피', '고추', '간지', '장스', '6초', '후라이드', '양념']

don = ['바삭치킨', '허니마라', '구운치킨', '구운핫', '구운마늘', '구운데리야끼', '구우바베큐', '매콤하니', '구운통다리', '구운순살치즈불닭', '구운순살치즈', '구운순살', '순살파닭', '콘베이크', '핫베이크', '구운양파솔솔', '구운커리솔솔', '후라이드간장', '후라이드양념', '후라이드']

twozone = ['핫쏘야', '불고기킹', '날개만만세', '한마리반반반', '미치고팔닭', '순살판타스틱', '어니언파닭', '눈코찡치킨', '눈치곳떡'] 

 kkanbu = ['마늘간장윙&봉크런치', '순살마늘간장', '핫바베큐윙&봉', '윙&봉크런치', '순살크리스피', '크리스피', '마늘전기구이', '마늘간장', '순살불사조', '순살스윗', '순살고추간장', '순살파닭', '전기구이', '바삭한식스팩', '후라이드']

 ggaenip = ['후라이드', '핫파스타', '양파크리미', '왕갈비', '양념', '칠리', '핫스파이스', '후레쉬갈릭', '눈꽃스윗치즈', '눈꽃허니버터', '간장', '눈꽃버터갈릭', '까르보나라', '파닭양념', '파닭후라이드', '고추쏘핫', '황금지단']

 dd = ['바삭후라이드', '핫후라이드', '순살', '매운불맛', '양념', '매운맛악마', '닭강정' ,'간장', '파닭', '까르보나라', '탕수', '토마토칠리']

 chickenmania = ['치즈블링', '순살파닭', '매니아윙', '매니아후라이드', '깐풍윙', '화이트블링', '새우', '간장', '양념', '후라이드반양념반']

 ho = ['치즈찐', '호차오', '치슐랭', '불닭', '후끈이', '데리갈릭', '바베큐', '치즈칠리로스트', '로스트', '어니언', '파닭', '간장', '반반', '양념', '크리스피']

 oven = ['로제', '하와이안', '요거닭', '까르보나라', '크런치', '썬크런치', '갈릭크러쉬', '칠리크러쉬', '반반메뉴크런치양념', '땡초야마늘아', '순살이치킨', '매콤아달콤아', '데리야끼', '허니갈릭크런치양념', '레드한크런치양념', '꾸닭크런치양념', '파닭', '블랙로스트', '레드로스트', '로스트']

choongman = ['후라이드', '매콤마늘양념', '마늘간장', '레드핫', '간장파닭', '매니아', '핫스노우어니언', '커리스노우어니언', '스노우어니언', '간장티꾸닭', '고추장티꾸닭', '커리티꾸닭', '신기고광', '충만아이티꾸', '베이컨스파니치', '티꾸간장똥집', '티꾸고추장똥집']

puradak = ['더차이나', '매드갈릭', '블랙알리오', '고추마요', '파불로', '스파이시걸스', '악마', '달콤양념']

hullala = ['순살참숯핫바베큐','쉬림프참숯바베큐','불갈비참숯바베큐','후라이드','양념','홀갈비참숯바베큐','고추','순살파닭바베큐','참숯핫바베큐','꿀간장치킨','투블랙간장바베큐','폭설치즈바베큐','참숯스위트바베큐','참숯치즈바베큐','마라순살바베큐','참숯대한바베큐','참숯데리바베큐','참숯갈릭바베큐','참숯치즈떡바베큐','참숯고구마떡바베큐','참숯소세지바베큐']

boor = ['크리스피','맛쇼킹순살','어니언순살','양념','델리','갈비만나','땡초순살','치즈스프린클','갈릭','파닭','맛쇼킹윙봉','부어텐더','골통삼총사','순살삼총사','두마리세트']

kyochon_dict = {}
for i in kyochon:
    kyochon_dict[i] = []
    for j in wording:
        if i in j:
        # 중복되는 치킨명이 있어 구분해줌

            if i == '레드콤보' or i == '양념' or i =='크리스피' or i == '후라이드': 
                if i in j and '교촌' not in j:
                    continue
            kyochon_dict[i].append(j)
    if kyochon_dict[i] == []:
        del kyochon_dict[i]

#메뉴가 캡션 갯수 확인
kyochon_main = []
for i in kyochon_dict:
    kyochon_main.append([i,len(kyochon_dict[i])])
kyochon_main = sorted(kyochon_main,key=(lambda x: x[1]),reverse = True)

#치킨 메뉴가 각 브랜드에서 차지하는 비중
from matplotlib import pyplot as plt
data = []
category = []
others = 0
sum1 = sum([y for x,y in kyochon_main])
for x,y in kyochon_main:
    if y < sum1/40:
        others += y
        continue
    category.append(x)
    data.append(y)
category.append('others')
data.append(others)
plt.pie(data,labels=category,radius = 2, autopct = '%0.1f%%')
plt.legend(category,bbox_to_anchor=(2,0,0,0))
plt.show()

#치킨 메뉴가 언급된 캡션 분석 후 워드클라우드 제작
kyochon_filter_wording = []
josa = ['하다','이다','있다'] 
stopwords = ['그램','타그램','맛스타그램','스타','먹스타','먹스타그램','인스타','스타','맛집','일상','소통','맞팔','선팔','먹스타그램','맛스타','낫다','먹스','맛스','아', '휴', '아이구', '아이쿠', '아이고', '어', '나', '우리', '저희', '따라', '의해', '을', '를', '에','없다', '의', '가', '으로', '너무','좋다', '로', '주다','에게', '뿐이다', '의거하여', '근거하여', '입각하여', '기준으로', '예하면', '예를 들면', '예를 들자면', '저', '소인', '소생', '저희', '지말고', '하지마', '하지마라', '다른', '물론', '또한', '그리고', '비길수 없다', '해서는 안된다', '뿐만 아니라', '만이 아니다', '만은 아니다', '막론하고', '관계없이', '그치지 않다', '그러나', '그런데', '하지만', '든간에', '논하지 않다', '따지지 않다', '설사', '비록', '더라도', '아니면', '만 못하다', '하는 편이 낫다', '불문하고', '향하여', '향해서', '향하다', '쪽으로', '틈타', '이용하여', '타다', '오르다', '제외하고', '이 외에', '이 밖에', '하여야', '비로소', '한다면 몰라도', '외에도', '이곳', '여기', '부터', '기점으로', '따라서', '할 생각이다', '하려고하다', '이리하여', '그리하여', '그렇게 함으로써', '하지만', '일때', '할때', '앞에서', '중에서', '보는데서', '으로써', '로써', '까지', '해야한다', '일것이다', '반드시', '할줄알다', '할수있다', '할수있어', '임에 틀림없다', '한다면', '등', '등등', '제', '겨우', '단지', '다만', '할뿐', '딩동', '댕그', '대해서', '대하여', '대하면', '훨씬', '얼마나', '얼마만큼', '얼마큼', '남짓', '여', '얼마간', '약간', '다소', '좀', '조금', '다수', '몇', '얼마', '지만', '하물며', '또한', '그러나', '그렇지만', '하지만', '이외에도', '대해 말하자면', '뿐이다', '다음에', '반대로', '반대로 말하자면', '이와 반대로', '바꾸어서 말하면', '바꾸어서 한다면', '만약', '그렇지않으면', '까악', '툭', '딱', '삐걱거리다', '보드득', '비걱거리다', '꽈당', '응당', '해야한다', '에 가서', '각', '각각', '여러분', '각종', '각자', '제각기', '하도록하다', '와', '과', '그러므로', '그래서', '고로', '한 까닭에', '하기 때문에', '거니와', '이지만', '대하여', '관하여', '관한', '과연', '실로', '아니나다를가', '생각한대로', '진짜로', '한적이있다', '하곤하였다', '하', '하하', '허허', '아하', '거바', '와', '오', '왜', '어째서', '무엇때문에', '어찌', '하겠는가', '무슨', '어디', '어느곳', '더군다나', '하물며', '더욱이는', '어느때', '언제', '야', '이봐', '어이', '여보시오', '흐흐', '흥', '휴', '헉헉', '헐떡헐떡', '영차', '여차', '어기여차', '끙끙', '아야', '앗', '아야', '콸콸', '졸졸', '좍좍', '뚝뚝', '주룩주룩', '솨', '우르르', '그래도', '또', '그리고', '바꾸어말하면', '바꾸어말하자면', '혹은', '혹시', '답다', '및', '그에 따르는', '때가 되어', '즉', '지든지', '설령', '가령', '하더라도', '할지라도', '일지라도', '지든지', '몇', '거의', '하마터면', '인젠', '이젠', '된바에야', '된이상', '만큼', '어찌됏든', '그위에', '게다가', '점에서 보아', '비추어 보아', '고려하면', '하게될것이다', '일것이다', '비교적', '좀', '보다더', '비하면', '시키다', '하게하다', '할만하다', '의해서', '연이서', '이어서', '잇따라', '뒤따라', '뒤이어', '결국', '의지하여', '기대여', '통하여', '자마자', '더욱더', '불구하고', '얼마든지', '마음대로', '주저하지 않고', '곧', '즉시', '바로', '당장', '하자마자', '밖에 안된다', '하면된다', '그래', '그렇지', '요컨대', '다시 말하자면', '바꿔 말하면', '즉', '구체적으로', '말하자면', '시작하여', '시초에', '이상', '허', '헉', '허걱', '바와같이', '해도좋다', '해도된다', '게다가', '더구나', '하물며', '와르르', '팍', '퍽', '펄렁', '동안', '이래', '하고있었다', '이었다', '에서', '로부터', '까지', '예하면', '했어요', '해요', '함께', '같이', '더불어', '마저', '마저도', '양자', '모두', '습니다', '가까스로', '하려고하다', '즈음하여', '다른', '다른 방면으로', '해봐요', '습니까', '했어요', '말할것도 없고', '무릎쓰고', '개의치않고', '하는것만 못하다', '하는것이 낫다', '매', '매번', '들', '모', '어느것', '어느', '로써', '갖고말하자면', '어디', '어느쪽', '어느것', '어느해', '어느 년도', '라 해도', '언젠가', '어떤것', '어느것', '저기', '저쪽', '저것', '그때', '그럼', '그러면', '요만한걸', '그래', '그때', '저것만큼', '그저', '이르기까지', '할 줄 안다', '할 힘이 있다', '너', '너희', '당신', '어찌', '설마', '차라리', '할지언정', '할지라도', '할망정', '할지언정', '구토하다', '게우다', '토하다', '메쓰겁다', '옆사람', '퉤', '쳇', '의거하여', '근거하여', '의해', '따라', '힘입어', '그', '다음', '버금', '두번째로', '기타', '첫번째로', '나머지는', '그중에서', '견지에서', '형식으로 쓰여', '입장에서', '위해서', '단지', '의해되다', '하도록시키다', '뿐만아니라', '반대로', '전후', '전자', '앞의것', '잠시', '잠깐', '하면서', '그렇지만', '다음에', '그러한즉', '그런즉', '남들', '아무거나', '어찌하든지', '같다', '비슷하다', '예컨대', '이럴정도로', '어떻게', '만약', '만일', '위에서 서술한바와같이', '인 듯하다', '하지 않는다면', '만약에', '무엇', '무슨', '어느', '어떤', '아래윗', '조차', '한데', '그럼에도 불구하고', '여전히', '심지어', '까지도', '조차도', '하지 않도록', '않기 위하여', '때', '시각', '무렵', '시간', '동안', '어때', '어떠한', '하여금', '네', '예', '우선', '누구', '누가 알겠는가', '아무도', '줄은모른다', '줄은 몰랏다', '하는 김에', '겸사겸사', '하는바', '그런 까닭에', '한 이유는', '그러니', '그러니까', '때문에', '그', '너희', '그들', '너희들', '타인', '것', '것들', '너', '위하여', '공동으로', '동시에', '하기 위하여', '어찌하여', '무엇때문에', '붕붕', '윙윙', '나', '우리', '엉엉', '휘익', '윙윙', '오호', '아하', '어쨋든', '만 못하다', '하기보다는', '차라리', '하는 편이 낫다', '흐흐', '놀라다', '상대적으로 말하자면', '마치', '아니라면', '쉿', '그렇지 않으면', '그렇지 않다면', '안 그러면', '아니었다면', '하든지', '아니면', '이라면', '좋아', '알았어', '하는것도', '그만이다', '어쩔수 없다', '하나', '일', '일반적으로', '일단', '한켠으로는', '오자마자', '이렇게되면', '이와같다면', '전부', '한마디', '한항목', '근거로', '하기에', '아울러', '하지 않도록', '않기 위해서', '이르기까지', '되다', '인해', '까닭으로', '이유만으로', '그래서', '이 때문에', '그러므로', '까닭', '있다', '결론을 낼 수 있다', '으로 인하여', '있다', '어떤것', '관계가 있다', '관련이 있다', '연관되다', '어떤것들', '에 대해', '이리하여', '그리하여', '여부', '하기보다는', '하느니', '하면 할수록', '운운', '이러이러하다', '하구나', '하도다', '다시말하면', '다음으로', '에 있다', '에 달려 있다', '우리', '우리들', '오히려', '하기는한데', '어떻게', '어떻해', '어찌됏어', '어때', '어째서', '본대로', '자', '이', '이쪽', '여기', '이것', '이번', '이렇게말하자면', '이런', '이러한', '이와 같은', '요만큼', '요만한 것', '얼마 안 되는 것', '이만큼', '이 정도의', '이렇게 많은 것', '이와 같다', '이때', '이렇구나', '것과 같이', '끼익', '삐걱', '따위', '와 같은 사람들', '부류의 사람들', '왜냐하면', '중의하나', '오직', '오로지', '에 한하다', '하기만 하면', '도착하다', '까지 미치다', '도달하다', '정도에 이르다', '할 지경이다', '결과에 이르다', '관해서는', '여러분', '하고 있다', '한 후', '혼자', '자기', '자기집', '자신', '우에 종합한것과같이', '총적으로 보면', '총적으로 말하면', '총적으로', '대로 하다', '으로서', '참', '그만이다', '할 따름이다', '쿵', '탕탕', '쾅쾅', '둥둥', '봐', '봐라', '아이야', '아니', '와아', '응', '아이', '참나', '년', '월', '일', '령', '영', '일', '이', '삼', '사', '오', '육', '륙', '칠', '팔', '구', '이천육', '이천칠', '이천팔', '이천구', '하나', '둘', '셋', '넷', '다섯', '여섯', '일곱', '여덟', '아홉', '령'] 
lemmatizer = Lemmatizer() 

for j in kyochon_dict['허니콤보']:
    j = j.replace(".","")
    j = j.replace('#','') 
    j = j.replace('치킨','')
    j = j.replace('교촌','')
    j = j.replace('허니콤보','')
    
    phrase = j.split()  
    for x in phrase:
        if x in josa or x in stopwords:
            break
        if lemmatizer.lemmatize(x) == []:
            if x in josa or x in stopwords:
                break
            kyochon_filter_wording.append(x)
        else:
            a = lemmatizer.lemmatize(x)
            for y in range(len(a)):
                if a[y][0] in josa or a[y][0] in stopwords:
                    break
                if a[y][1]=='Adjective' or a[y][1]== 'Verb':
                    if a[y][0] not in josa and a[y][0] not in stopwords:
                        kyochon_filter_wording.append(a[y][0])
                        break
                else: 
                    if a[0][0] not in josa and a[0][0] not in stopwords:
                        kyochon_filter_wording.append(a[0][0])
temp = kyochon_filter_wording
kyochon_filter_wording = []
okt = Okt()
tags = []

for j in temp:
    morph = okt.pos(j)
    tags.append(morph)
tags

for sentence in tags:
        for word,tag in sentence:
            if tag in ['Noun','Adjective','Adverb']:
                kyochon_filter_wording.append(word)
                break
                
kyochon_filter_word = Counter(kyochon_filter_wording)
kyochon_filter_word = kyochon_filter_word.most_common()

wc = WordCloud(font_path = '/Users/leejeongyeob/Library/Fonts/IropkeBatangM.ttf', \
               background_color = "white", \
               width = 1000, \
               height = 1500, \
               colormap="CMRmap",\
               max_words = 3000)
wc.generate_from_frequencies(dict(kyochon_filter_word))
wc.to_file('교촌허니콤보_keyword.png')
      