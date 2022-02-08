import imaplib
import email
import re
import datetime
from threading import Thread
from lxml import etree
from bs4 import BeautifulSoup
from simplejson import load
from login import Account
from query import Query
import uuid
import os

th_arr = {}
filename_out = os.path.dirname(os.path.realpath(__file__)) + "/" + datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")+".txt"


DEBUG = True
def read_letters(username, password):
    # Login to INBOX
    try:
        account = Account(username, password, type=0)
    except Exception as e:
        print(e)
        return []
    ids = ""
    try:
        query = Query(account)
        query.select_folder("INBOX")
        ids = query.parse_unread_ids()
    except Exception as e:
        print(e)
        return []

    
    if not ids:
        return []
    res = []
    for i in query.get_letters_by_ids(ids):
        if DEBUG:
            filename = str(uuid.uuid4())+".html"
            with open('debug/{0}'.format(filename),'w+') as f:
                f.write(i.sendler+"\n"*4+i.get_msg())
        for item in i.get_links():
            res.append(item)

    return res
    
    



accs = """
ValentinZolotarev9350@rambler.ru	bvjtgxup_A9350
GennadiiGlebov9764@rambler.ru	pnvngigb_A9764
YAroslavZlobin6467@rambler.ru	whpmjflt_A6467
DaniilDrujinin5313@rambler.ru	trkppnmv_A5313
PavelErmolaev4236@rambler.ru	hcpyywjy_A4236
RuslanErofeev5417@rambler.ru	sobnmxdm_A5417
MihailEgorov9949@rambler.ru	ylhvoqjj_A9949
GrigoriiBelov6573@rambler.ru	bprjgdto_A6573
RuslanVeshnyakov8488@rambler.ru	zginncdu_A8488
NikitaJukov7590@rambler.ru	iiijcakq_A7590
IvanGusev6285@rambler.ru	oamhfydp_A6285
GlebDemidov6968@rambler.ru	wyuejhll_A6968
BogdanAgafonov9527@rambler.ru	atcahrvv_A9527
StanislavBogomolov1810@rambler.ru	pcqddxng_A1810
DaniilBulgakov7526@rambler.ru	alamxnoj_A7526
BorisZuev8895@rambler.ru	occwopbf_A8895
GeorgiiIzmailov8548@rambler.ru	ltdhsive_A8548
VitaliiAndrianov6603@rambler.ru	edvebhnd_A6603
KonstantinGulyaev3765@rambler.ru	xeazmbwj_A3765
RomanDorofeev6120@rambler.ru	aidcgvlx_A6120
AlekseiAleshin4226@rambler.ru	ffnmdgcy_A4226
BogdanGluhov8144@rambler.ru	krzxtabn_A8144
IgorBelozerov4966@rambler.ru	xdprmwii_A4966
VladimirIlinskii8638@rambler.ru	gakwnqqm_A8638
VladimirDemidov3627@rambler.ru	jostaaht_A3627
PetrDubinin2352@rambler.ru	sknmigng_A2352
BorisKirillov1716@rambler.ru	jqkabyyw_A1716
BogdanKalugin8125@rambler.ru	tvaxqqvy_A8125
AleksandrBragin1639@rambler.ru	smwokslj_A1639
BorisBobylev3007@rambler.ru	ttxglzzk_A3007
MaksimElizarov4031@rambler.ru	bvrlevoz_A4031
KirillZelenin7275@rambler.ru	cvzamvtp_A7275
AntonVorobev5905@rambler.ru	rlnbkxvv_A5905
DenisBogomolov2145@rambler.ru	jkrzmzet_A2145
MaksimZvyagincev3478@rambler.ru	xlsyscbl_A3478
VladimirIgnatev5041@rambler.ru	nfatcgib_A5041
KonstantinBelkin4486@rambler.ru	srmtzkpz_A4486
StanislavVorobev2605@rambler.ru	zqiozilj_A2605
GeorgiiKazakov8387@rambler.ru	kqxqbcxu_A8387
RuslanDyachkov2942@rambler.ru	gezdlopy_A2942
DaniilErshov8743@rambler.ru	jkfwjwus_A8743
NikitaDrujinin6127@rambler.ru	vbfogcqi_A6127
GeorgiiGladkov8491@rambler.ru	gcpkzocf_A8491
VladimirBelozerov1191@rambler.ru	wxxghpxm_A1191
IlyaAgafonov6785@rambler.ru	yenihiki_A6785
MatveiVoronov6510@rambler.ru	eeztwlqd_A6510
BogdanArtemev8819@rambler.ru	jkfuegce_A8819
AleksandrAlehin8963@rambler.ru	phmtmbvu_A8963
GennadiiArtemov6506@rambler.ru	obmkobhi_A6506
AlekseiGladkov2084@rambler.ru	mydzccho_A2084
IgorGorlov2202@rambler.ru	ilvnzgvc_A2202
KirillBlohin4391@rambler.ru	xifjzwyq_A4391
KirillEremin6936@rambler.ru	xchspwmx_A6936
BogdanVishnyakov5911@rambler.ru	jlamjmxu_A5911
RuslanDorohov8889@rambler.ru	mynfthba_A8889
EgorVolkov2824@rambler.ru	nzcrbxgt_A2824
AntonGorunov5961@rambler.ru	inbtaeil_A5961
StanislavGluhov1405@rambler.ru	tmyvfavo_A1405
VitaliiEvdokimov4177@rambler.ru	jpuxlcav_A4177
EvgeniiDyachkov5019@rambler.ru	bmoedlns_A5019
BogdanAgeev7281@rambler.ru	upycctoy_A7281
KirillGorelov9858@rambler.ru	yfuniici_A9858
PavelBalashov9967@rambler.ru	nyluloth_A9967
ValeriiEmelyanov5077@rambler.ru	xetakgno_A5077
AntonBasov6141@rambler.ru	assgnqey_A6141
YAroslavBoldyrev7412@rambler.ru	oafhcezm_A7412
IlyaDubrovin1927@rambler.ru	ylzwoeez_A1927
ValeriiBykov9990@rambler.ru	nzogvmmb_A9990
YAroslavEvseev3998@rambler.ru	cvsomsyf_A3998
GeorgiiBelozerov1646@rambler.ru	qjizuzxc_A1646
IgorGalkin2522@rambler.ru	qkekzree_A2522
AntonGlebov7256@rambler.ru	geypjyof_A7256
StanislavGoncharov5086@rambler.ru	nvhesnwq_A5086
EvgeniiDemidov1510@rambler.ru	aqqqmihv_A1510
ViktorBorisov5731@rambler.ru	hitzidlp_A5731
KirillEremeev2969@rambler.ru	mxwbifql_A2969
AntonZolotov4278@rambler.ru	nayaswgb_A4278
NikitaZavyalov6017@rambler.ru	xdkzhovz_A6017
GennadiiVinogradov1198@rambler.ru	bosbdnge_A1198
DenisBezrukov2782@rambler.ru	cvaqwhhi_A2782
RuslanKartashov5693@rambler.ru	mzjakyww_A5693
StanislavIlin9571@rambler.ru	wdphywql_A9571
RuslanGlebov5920@rambler.ru	exljlqap_A5920
PavelEfremov5722@rambler.ru	botrktcz_A5722
DmitriiEmelyanov1425@rambler.ru	pihbhsed_A1425
VladimirZelenin4772@rambler.ru	hoikwdlc_A4772
VasiliiAbramov4554@rambler.ru	xkkysoqj_A4554
ValentinEremeev4451@rambler.ru	nyskblph_A4451
AlekseiGlebov8774@rambler.ru	pdgddusk_A8774
StanislavAntipov2697@rambler.ru	tnszohhe_A2697
DenisAntipov6248@rambler.ru	mwckzlcn_A6248
IvanDolgov9092@rambler.ru	rrljjdfz_A9092
ValentinVeselov2190@rambler.ru	qfxtnhzu_A2190
RomanGerasimov6513@rambler.ru	wwrzarfw_A6513
IgorEvseev2256@rambler.ru	peuqjgjp_A2256
GlebBobylev6077@rambler.ru	wdjamifv_A6077
IvanAleshin7695@rambler.ru	ghbnpaip_A7695
ValeriiBelyakov6995@rambler.ru	mtticsql_A6995
DmitriiVlasov3787@rambler.ru	cxuoeksv_A3787
EgorGorunov3312@rambler.ru	kwodolnr_A3312
EvgeniiDorofeev5152@rambler.ru	zgbbnamy_A5152
EvgeniiKazakov6136@rambler.ru	iphgiocj_A6136
DmitriiJdanov4038@rambler.ru	ezdnxsfl_A4038
MihailBobylev6615@rambler.ru	oblbjmfv_A6615
AntonErmilov4887@rambler.ru	offpuejy_A4887
BogdanGrachev1603@rambler.ru	rmrxhqle_A1603
IlyaKarpov2830@rambler.ru	ubtkbocx_A2830
MatveiGerasimov9965@rambler.ru	ffifrpgb_A9965
BorisBulgakov4450@rambler.ru	gkynpjqq_A4450
VitaliiBajenov3821@rambler.ru	atkoomnc_A3821
DenisGorbachev9064@rambler.ru	lyoieosc_A9064
VladimirIlin5364@rambler.ru	dxrfbfwx_A5364
AntonVorobev8167@rambler.ru	ohrmygyq_A8167
RuslanBulgakov7889@rambler.ru	mzwgyhre_A7889
VladimirDubov9584@rambler.ru	krtawruk_A9584
BogdanAnikin7311@rambler.ru	qjbnvbrk_A7311
MaksimVavilov7774@rambler.ru	qpmstoyj_A7774
PetrJuravlev7694@rambler.ru	xjpgjvii_A7694
GlebZaicev6932@rambler.ru	swhvhaxt_A6932
RomanEliseev7906@rambler.ru	penfmlls_A7906
AlekseiZolotov1250@rambler.ru	jplguefb_A1250
StanislavAbramov8898@rambler.ru	ritrjgjq_A8898
IlyaIzmailov7158@rambler.ru	qjbozoft_A7158
MatveiAstahov4365@rambler.ru	ediyqegf_A4365
EgorBocharov3962@rambler.ru	bvmubtre_A3962
NikitaAndreev2144@rambler.ru	ssbtdxtu_A2144
RuslanBogomolov9656@rambler.ru	cwolkcuk_A9656
RomanGorbunov1058@rambler.ru	fdcqafpi_A1058
RuslanDenisov1910@rambler.ru	ipczupeg_A1910
GennadiiEremeev9536@rambler.ru	msayvcab_A9536
EgorDoronin4512@rambler.ru	kymsxldd_A4512
DenisJdanov9806@rambler.ru	nznfvnud_A9806
DenisBespalov2527@rambler.ru	houaaylz_A2527
ValeriiEremeev2377@rambler.ru	ikscwdkq_A2377
RuslanArtemev2866@rambler.ru	musrooxn_A2866
IlyaJuravlev6284@rambler.ru	hozgeofa_A6284
VladimirKarasev8768@rambler.ru	ozuyzpgf_A8768
DaniilVoloshin9056@rambler.ru	xzjqnhtu_A9056
VladimirGoryachev8274@rambler.ru	jpukkmrv_A8274
RuslanVereshchagin6922@rambler.ru	fxmlsjzx_A6922
GeorgiiVoronkov2177@rambler.ru	xzxailru_A2177
KirillBelyakov1473@rambler.ru	ineloczz_A1473
DmitriiGordeev6365@rambler.ru	tshedbuy_A6365
GennadiiVdovin2195@rambler.ru	edwsgfpw_A2195
MaksimGluhov8228@rambler.ru	ynxzcdfe_A8228
DaniilVlasov9758@rambler.ru	anrcjlbf_A9758
VitaliiJarov4968@rambler.ru	exwwdekr_A4968
IlyaDolgov1251@rambler.ru	zrswzpkr_A1251
DmitriiBelov2435@rambler.ru	aqkxfvih_A2435
NikitaErmilov2590@rambler.ru	rmjwevjn_A2590
GennadiiZelenin6651@rambler.ru	xlanbels_A6651
VitaliiBocharov7200@rambler.ru	phwapwlz_A7200
NikitaAstafev8100@rambler.ru	cuqvvlfr_A8100
YAroslavDanilov1624@rambler.ru	bxfegyzt_A1624
DenisKabanov5418@rambler.ru	lxenfvvy_A5418
VladimirVishnevskii2898@rambler.ru	hgfsynbm_A2898
AleksandrElizarov6015@rambler.ru	nftypgac_A6015
DaniilBessonov4688@rambler.ru	ymngkhas_A4688
AntonAkimov6885@rambler.ru	zqjfmfiw_A6885
MihailDemyanov8649@rambler.ru	mavaaklm_A8649
RomanVladimirov5541@rambler.ru	hhrvxdwc_A5541
BorisJukov3122@rambler.ru	qlembyto_A3122
VladimirKalashnikov5043@rambler.ru	bujmgpcq_A5043
EvgeniiDemidov2100@rambler.ru	bonkbnpe_A2100
KonstantinGluhov4945@rambler.ru	fzckpzmc_A4945
KonstantinAbramov9443@rambler.ru	atbzejdc_A9443
KonstantinDorohov4014@rambler.ru	wdwrrfgt_A4014
IlyaAnohin5016@rambler.ru	joltxzgy_A5016
VladimirZinovev2789@rambler.ru	famqhiqq_A2789
DmitriiZorin5969@rambler.ru	lalgebqh_A5969
MaksimGoryachev1347@rambler.ru	mtypoijx_A1347
VasiliiAvdeev5092@rambler.ru	xfxoztul_A5092
VasiliiBelikov5080@rambler.ru	veolqhzf_A5080
DmitriiIsaev9904@rambler.ru	xjcnxgji_A9904
YAroslavZelenin3899@rambler.ru	jpsrszfe_A3899
MatveiBabushkin1180@rambler.ru	ginsxqyv_A1180
MatveiZaicev1128@rambler.ru	vafewlah_A1128
KonstantinGribov5248@rambler.ru	trludyjd_A5248
VladimirAntipov4302@rambler.ru	qmavxpzf_A4302
DenisKarpov7722@rambler.ru	pciptsub_A7722
RomanGerasimov1517@rambler.ru	inelpgjc_A1517
GlebGusev2301@rambler.ru	jnwjelkg_A2301
AlekseiZykov5675@rambler.ru	eeccwcwm_A5675
PetrBykov1337@rambler.ru	fyuzvsgg_A1337
IlyaBezrukov5222@rambler.ru	zhejicvv_A5222
GrigoriiBurov1198@rambler.ru	ngyzcwcp_A1198
ViktorBorisov4683@rambler.ru	ewvsxtrg_A4683
IlyaBoldyrev1492@rambler.ru	vceufieb_A1492
MatveiEfremov9644@rambler.ru	rqeifepv_A9644
RuslanKireev8870@rambler.ru	boyuiscl_A8870
VladimirGrekov2904@rambler.ru	buxgsdur_A2904
RuslanBlohin3836@rambler.ru	phppscqm_A3836
DaniilAstahov7488@rambler.ru	dcolaslz_A7488
EvgeniiZorin8113@rambler.ru	ashuvduv_A8113
AlekseiIsakov6748@rambler.ru	menegpxo_A6748
BogdanIgnatev9695@rambler.ru	fbcqlrhv_A9695
VasiliiEfremov2841@rambler.ru	qppnuzfu_A2841
ValentinGubanov2981@rambler.ru	cpjtvxxb_A2981
DaniilIgnatev3534@rambler.ru	phrwmive_A3534
StanislavJukov8589@rambler.ru	tnklfeqa_A8589
GennadiiBychkov5175@rambler.ru	dxrfeqgy_A5175
KirillGorlov4931@rambler.ru	pinjukbv_A4931
GrigoriiVolkov7427@rambler.ru	amcqisss_A7427
GlebKireev8435@rambler.ru	fagitnju_A8435
IlyaBorisov5177@rambler.ru	jixihthq_A5177
PetrVereshchagin6222@rambler.ru	ubzspjfh_A6222
"""
RAMBLER = 0
MAILRU= 1
r = []
cnt = 0
for item in accs.split("\n"):
    if item == "":
        continue
    cnt += 1
    print("Started {0} of {1}".format(cnt, len(accs.split("\n"))-2))
    t = item.split("	")
    if len(t) < 2:
        print("error in line {0}".format(accs))
        continue
    
    login, password = t[0], t[1]
    for i in read_letters(login, password):
        r.append(i)
    with open(filename_out, "w+") as f:
        f.write("\n".join(r))
    
    

