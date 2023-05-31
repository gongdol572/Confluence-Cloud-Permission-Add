from base64 import encode
import requests
import time
import json
from tabulate import tabulate

###############권한 부여 체크 #################

def addpermission(permissionkey,permissionlist,permissionadd):
   print("permission key size =", len(permissionkey))

   for i in range (0,len(permissionkey)):
      if(permissionkey[i]=='1-1' or permissionkey[i]=='1-all'):
         permissionadd+=[[permissionlist[0][0],permissionlist[0][1]]]
         print(permissionadd)
      elif(permissionkey[i]=='2-1'):
         permissionadd+=[[permissionlist[1][0],permissionlist[1][1]]]
      elif(permissionkey[i]=='2-2'):
         permissionadd+=[[permissionlist[1][0],permissionlist[1][2]]]
      elif(permissionkey[i]=='2-3'):
         permissionadd+=[[permissionlist[1][0],permissionlist[1][3]]]
      elif(permissionkey[i]=='2-4'):
         permissionadd+=[[permissionlist[1][0],permissionlist[1][4]]]
      elif(permissionkey[i]=='3-1'):
         permissionadd+=[[permissionlist[2][0],permissionlist[2][1]]]
      elif(permissionkey[i]=='3-2'):
         permissionadd+=[[permissionlist[2][0],permissionlist[2][1]]]
      elif(permissionkey[i]=='3-3'):
         permissionadd+=[[permissionlist[2][0],permissionlist[2][2]]]
      elif(permissionkey[i]=='3-4'):
         permissionadd+=[[permissionlist[2][0],permissionlist[2][3]]]
      elif(permissionkey[i]=='3-5'):
         permissionadd+=[[permissionlist[2][0],permissionlist[2][4]]]
      elif(permissionkey[i]=='4-1' or permissionkey[i]=='4-all'):
         permissionadd+=[[permissionlist[3][0],permissionlist[3][1]]]
      elif(permissionkey[i]=='5-1' or permissionkey[i]=='5-all'):
         permissionadd+=[[permissionlist[4][0],permissionlist[4][1]]]
      elif(permissionkey[i]=='6-1' or permissionkey[i]=='6-all'):
         permissionadd+=[[permissionlist[5][0],permissionlist[5][1]]]
      elif(permissionkey[i]=='7-1' or permissionkey[i]=='7-all'):
         permissionadd+=[[permissionlist[6][0],permissionlist[6][1]]]
      elif(permissionkey[i]=='2-all'):
         for i in range(0,len(permissionlist[1])-1):
            permissionadd+=[[permissionlist[1][0],permissionlist[1][i+1]]]
      elif(permissionkey[i]=='3-all'):
         for i in range(0,len(permissionlist[2])-1):
            permissionadd+=[[permissionlist[2][0],permissionlist[2][i+1]]]
      elif(permissionkey[i]=='all'):
         permissionadd+=permissionlist
      else:
         permissionkey=input("권한을 잘못 입력했습니다. 다시 입력해주세요").split(',')
         addpermission(permissionkey,permissionlist,permissionadd)
         
      
#적용 권한 리턴
   return permissionadd





###############################################################################################################3

#권한 부여 함수

def grantpermission(permissionadd, usertype, identifier):

   for i in range (0,size):
      
      # 권한 부여를 위한 Rest API Call 호출 
      url = "https://<Confluence Site 주소 입력>/wiki/rest/api/space/" + space[i][0] + "/permission"
      print(time.strftime('%x %X'), "권한 작업할 스페이스 key = " + space[i][0])
      print(time.strftime('%x %X'), "권한 작업할 스페이스 key = " + space[i][0], file=logfile)
      print(time.strftime('%x %X'), "작업할 권한  = " + permissionadd[i][0] + ','+ permissionadd[i][1])
      print(time.strftime('%x %X'), "작업할 권한  = " + permissionadd[i][0] + ','+ permissionadd[i][1], file=logfile)


      headers = {
      "Accept" : "application/json",
      "Content-Type" : "application/json",
      "Authorization" : "Bearer 토큰 입력 "
      }
      
      payload = json.dumps( {
         "subject": {
            "type": "{}".format(usertype),
            "identifier": "{}".format(identifier)
            },
            "operation": {
               "key": "{}".format(permissionadd[i][0]),
               "target": "{}".format(permissionadd[i][1])
               },
               "_links": {}
               } )

      response = requests.request(
         "POST",
         url,
         data=payload,
         headers=headers
         )

      
     

#권한 작업 실패 시 작업 실패와 함께 http 상태 코드, 에러메세지 출력
      if(response.status_code !=200):
         print(time.strftime('%x %X'), "권한 추가 작업이 실패했습니다.\n 내용 : {}".format(json.loads(response.text)["message"]))
         print(time.strftime('%x %X'), "http 코드 : ",response.status_code)
         print(time.strftime('%x %X'), "권한 추가 작업이 실패했습니다.\n 내용 : {}".format(json.loads(response.text)["message"]),file=logfile)
         print(time.strftime('%x %X'), "http 코드 : ",response.status_code, file=logfile)
#권한 작업 성공 시 작업 성공과 함께 http 상태 코드, 에러메세지 출력
      else:
         print(time.strftime('%x %X'), "권한 추가 작업이 성공했습니다. \n ")
         print("권한 id : {} \n 권한 키: {} \n ".format( json.dumps(json.loads(response.text)["id"]),permissionkey))
         print(time.strftime('%x %X'), "스페이스 권한 추가 rest 결과 :" ,json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
         print(time.strftime('%x %X'), "스페이스 권한 추가 rest 결과 :" ,json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")),file=logfile)
         print(time.strftime('%x %X'), "http 코드 : ",response.status_code, file=logfile)
         
      print("=====================================작업 완료선 ======================================",file=logfile)



############################################################################

url = "https://<Confluence Site 주소 입력>/wiki/rest/api/space?type=global&limit=1000"

#log 파일 쓰기 모드로 불러오기
logfile= open('C:/Users/Jackson/Desktop/restresult.log','a')


# Atlassian Cloud User API Token 발급 방법 : https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/

headers = {
   "Accept": "application/json",
   "Authorization" : "<Atlassian Bearer Token 입력>"
}

response = requests.request(
   "GET",
   url,
   headers=headers
)



# CQL 결과 값 JSON 형식으로 출력
print(time.strftime('%x %X'), "스페이스 리스트 rest 조회 결과 :", json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
# print(time.strftime('%x %X'), "스페이스 리스트 rest 조회 결과 :", json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")),file=logfile)


#json에서 스페이스 총합 갯수 가져오기
size=int(json.loads(response.text)["size"])


#스페이스 갯수 출력
print(time.strftime('%x %X'), "스페이스 갯수 = ",size, file=logfile)
print(time.strftime('%x %X'), "스페이스 갯수 = ",size)

#스페이스 키 배열 추가를 위한 배열 설정

space=[]
for i in range (0,size):
       #json에서 가져온 key 값 추가
       space+=[[json.loads(response.text)["results"][i]['key'],json.loads(response.text)["results"][i]['name']]]
      



print(time.strftime('%x %X'), "스페이스 이름: \n",tabulate(space))


permissionlist=[['read','space'],['create','page','blogpost','comment','attachment'],['delete','page','blogpost','comment','attachment','space'],['export','space'],['administer','space'],['archive','page'],['restrict_content','space']]

# 스페이스 권한 설정에 대한 전체 권한 리스트 출력
print("부여할 권한을 선택하세요. 번호로 입력해 주시면 됩니다.")
print(tabulate(permissionlist,tablefmt='grid'))
print("사용 방법 : 1-1,1-2 식으로 입력하시면 됩니다.")
print("")


# 추가할 권한을 , 을 비교로 권한 추가
permissionkey=input("권한 입력 : ").split(',')

# 권한을 적용할 리스트 추가
permissionadd=[]

#permission key를 기반으로 권한 적용 함수에 대입
addpermission(permissionkey,permissionlist,permissionadd)

print("부여할 권한을 체크하고 있습니다. \n 적용할 권한이 맞는지 확인해주세요. 네, 아니요, y, n 식으로 입력해주세요 \n ")
print(tabulate(permissionadd))
permissoncheck=input("입력한 권한이 맞으신가요 ?")

# 선택한 권한이 아닐 경우  n 키나 아니요 키를 입력하여 값을 다시 입력 받도록 함.
while (permissoncheck=='아니요' or permissoncheck=='no' or permissoncheck=='n'):
   permissionkey=input("다신 권한을 입력해주세요 : ").split(',')
   permissionadd=[]
   addpermission(permissionkey,permissionlist,permissionadd)
   print("부여할 권한을 체크하고 있습니다. \n 적용할 권한이 맞는지 확인해주세요. 네, 아니요, y, n 식으로 입력해주세요 \n ")
   print(tabulate(permissionadd))
   permissoncheck=input("입력한 권한이 맞으신가요 ?")



print("권한 적용을 확인하였습니다. 권한을 적용할 사용자 유형과 대상을 작성해주세요 \n 예: 사용자 유형: user 또는 group, 대상: jackson")

# 권한을 적용할 사용자 또는 그룹 추가
usertype=input("사용자 유형: ")
identifier=input("대상: ")
usercheck=input("부여할 사용자 대상이 아래와 같나요? yes or no로 입력해주세요  \n 사용자 유형 : {} \n 대상 : {} \n 여기에 값을 입력해주세요 :  ".format(usertype, identifier))

# 적용할 사용자를 잘못 적용할 경우 재 적용
while usercheck=='아니요' or usercheck=='no' or usercheck=='n':
   usertype=input("사용자 유형:")
   identifier=input("대상")
   print("부여할 사용자 대상이 아래와 같나요? yes or no로 입력해주세요  \n 사용자 유형 : {} \n 대상 : {} ".format(usertype, identifier))
   usercheck=input()

# 최종 권한 적용.

for i in range(0,len(permissionadd)):
   grantpermission(permissionadd, usertype, identifier)




