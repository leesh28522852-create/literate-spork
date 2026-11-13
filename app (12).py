"""스프라우트 카트 — GitHub + Streamlit Community Cloud
Python 3.11+. app.py와 requirements.txt를 같은 저장소에 업로드하고 app.py 배포.
로컬: pip install -r requirements.txt && streamlit run app.py
3D 엔진은 브라우저가 jsDelivr CDN에서 가져옵니다. 인터넷·WebGL이 필요합니다.
회원가입/API 키/게임 서버 불필요. AI는 브라우저에서 계산합니다.
실제 자유주행 시뮬레이터가 아닌 코스 진행 방향 보조가 있는 아케이드 레이싱입니다.
"""
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title='스프라우트 카트', page_icon='🏎️', layout='wide', initial_sidebar_state='collapsed')
st.markdown('''<style>.block-container{padding-top:.5rem;padding-bottom:0;max-width:1500px}header[data-testid="stHeader"]{height:0;visibility:hidden}.stApp{background:#0a1423;color:white}iframe{border:0}</style>''', unsafe_allow_html=True)
GAME = r'''<!DOCTYPE html>
<html lang="ko"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1"><title>스프라우트 카트</title>
<style>
*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#0a1423;color:#fff;font-family:system-ui,'Apple SD Gothic Neo',sans-serif}#game{position:relative;width:100%;height:100%;min-height:550px;outline:none;touch-action:none}canvas{display:block;width:100%;height:100%}.layer{position:absolute;inset:0;pointer-events:none}#hud{display:flex;justify-content:space-between;align-items:flex-start;padding:14px;gap:10px}.glass{background:#102434de;border:1px solid #ffffff35;border-radius:16px;box-shadow:0 8px 28px #0003;padding:12px 16px;backdrop-filter:blur(9px)}.big{font-weight:900;font-size:28px;color:#c7ff78}.small{font-size:12px;color:#d3e5ef}.pill{border-radius:20px;padding:7px 12px;background:#234756;margin-top:7px;font-size:13px}.bar{height:8px;background:#081a26;border-radius:8px;overflow:hidden;margin-top:7px}.fill{height:100%;width:0%;background:linear-gradient(90deg,#9bed9c,#d9ff79)}#toast{position:absolute;top:150px;width:100%;text-align:center;font-weight:800;text-shadow:0 2px 6px #000;pointer-events:none}#count{position:absolute;inset:0;display:grid;place-items:center;font-size:110px;font-weight:1000;text-shadow:0 8px 0 #264756;pointer-events:none;color:#efffa9}.overlay{position:absolute;inset:0;background:linear-gradient(140deg,#0b203cba,#0c2736b8);display:flex;align-items:center;justify-content:center;padding:16px;z-index:5;overflow:auto}.panel{width:min(520px,100%);padding:28px;border-radius:24px;background:#102337ec;border:1px solid #b8fba04d;box-shadow:0 24px 80px #0007}h1{font-size:clamp(30px,6vw,49px);line-height:1.05;margin:12px 0;color:#d2ff87}h2{margin:0 0 16px}.tag{font-size:12px;color:#abe6ca;letter-spacing:3px}.lead{color:#d4e5ee;line-height:1.7}button{border:0;border-radius:12px;font:700 15px system-ui;cursor:pointer;color:#0b2330;background:#d1ff88;padding:13px 18px;touch-action:none}button.secondary{background:#29485c;color:#fff}button:focus-visible{outline:3px solid #fff;outline-offset:3px}button:active{transform:scale(.96)}.row{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}.hidden{display:none!important}#utility{position:absolute;bottom:170px;right:12px;display:flex;gap:6px;z-index:3}#utility button{padding:9px;font-size:12px;background:#143344db;color:#fff;border:1px solid #ffffff3b}#controls{position:absolute;bottom:20px;left:0;right:0;display:flex;justify-content:space-between;align-items:flex-end;padding:0 16px;pointer-events:none;z-index:2}.pad{display:flex;gap:8px;align-items:flex-end}.stack{display:flex;flex-direction:column;gap:8px}.ctrl{pointer-events:auto;width:58px;height:58px;padding:0;background:#153e53d9;border:1px solid #a4cee080;color:#fff;user-select:none;-webkit-user-select:none}.ctrl.accent{background:#ccff91e8;color:#153342}.ctrl.wide{width:72px}.ctrl.pressed{background:#fff;color:#0c2838}#laps{max-height:85px;overflow:auto;font-size:12px;margin-top:6px}#leader{font-size:12px;margin-top:8px;line-height:1.8}table{width:100%;border-collapse:collapse;font-size:14px}td{padding:10px 4px;border-bottom:1px solid #ffffff25}.hint{font-size:12px;color:#bfd1e2;line-height:1.6}.error{background:#402d3e;color:#fff;padding:20px;border-radius:16px}#speed{font-size:24px}#load{position:absolute;inset:0;display:grid;place-items:center;background:#0d2439;z-index:8;padding:30px;text-align:center}
@media(max-width:600px){#hud{padding:8px;gap:6px}.glass{padding:10px;border-radius:12px}.big{font-size:23px}.panel{padding:22px}.ctrl{width:47px;height:52px}.ctrl.wide{width:61px}.pad{gap:5px}#controls{padding:0 8px;bottom:16px}#leader{font-size:11px}#utility{bottom:152px}#toast{top:165px;font-size:14px}.small{font-size:11px}}
@media(prefers-reduced-motion:reduce){*{scroll-behavior:auto}}
</style></head><body>
<div id="game" tabindex="0" aria-label="스프라우트 카트 3D 레이싱 게임">
<div id="load"><div>🌱 스프라우트 카트<br><br>3D 트랙을 불러오는 중…<p class="hint">인터넷 연결과 WebGL이 필요합니다.</p></div></div>
<div class="layer" id="hud"><div class="glass"><div class="small">CLOVER COAST · 클로버 해안</div><div class="big"><span id="rank">1</span><span style="font-size:14px;color:white"> / 4위</span></div><div id="leader"></div></div><div class="glass" style="min-width:130px"><div class="small">LAP <b id="lap">1 / 3</b></div><div id="time" style="font-weight:800;font-variant-numeric:tabular-nums">00:00.000</div><div id="speed">0 <small style="font-size:11px">km/h</small></div><div class="small">부스터 <span id="boostval">25</span>%</div><div class="bar"><div class="fill" id="boostbar"></div></div><div id="item" class="pill">아이템 없음</div><div id="laps"></div></div></div>
<div id="toast"></div><div id="count"></div>
<div id="utility"><button id="pause">일시정지</button><button id="full">전체화면</button></div>
<div id="controls"><div class="pad"><button class="ctrl" data-key="ArrowLeft" aria-label="왼쪽">◀</button><button class="ctrl" data-key="ArrowRight" aria-label="오른쪽">▶</button><button class="ctrl wide" data-key="Space">드리프트</button></div><div class="pad"><div class="stack"><button class="ctrl wide" data-key="KeyE">아이템</button><button class="ctrl wide accent" data-key="ShiftLeft">부스터</button></div><div class="stack"><button class="ctrl accent" data-key="ArrowUp">가속</button><button class="ctrl" data-key="ArrowDown">감속</button></div></div></div>
<div id="start" class="overlay"><div class="panel"><div class="tag">ORIGINAL ARCADE RACER</div><h1>SPROUT<br>KART 🌱</h1><p class="lead">작은 새싹 레이서의 커다란 해안 레이스.<br>클로버 해안에서 AI 3대와 3바퀴 대결!</p><div class="hint">↑ 가속 · ↓ 감속 · ← → 조향<br>Space 드리프트 · Shift 부스터 · E 아이템<br>모바일은 아래 터치 버튼을 동시에 누르세요.<br>코스 방향 보조가 있어 조향은 좌우 위치를 조절합니다.<br>드리프트를 유지하면 부스터가 더 빨리 충전됩니다.</div><div class="row"><button id="startBtn">🏁 레이스 시작</button><button id="quality" class="secondary">화질: 기본</button></div><p id="best" class="hint"></p><p class="hint">화면을 한 번 누르면 키보드 조작이 연결됩니다.<br>로그인·결제·실시간 멀티플레이 없이 플레이합니다.</p></div></div>
<div id="paused" class="overlay hidden"><div class="panel"><h2>잠깐 쉬어 가요</h2><p class="lead">경기와 시간 측정을 멈췄습니다.</p><div class="row"><button id="resume">계속 달리기</button><button id="restartPause" class="secondary">처음부터</button></div></div></div>
<div id="result" class="overlay hidden"><div class="panel"><div class="tag">FINISH LINE</div><h1 id="resultTitle">완주!</h1><p class="lead" id="resultTime"></p><div id="resultTable"></div><p class="hint" id="resultLaps"></p><div class="row"><button id="again">다시 하기</button><button id="home" class="secondary">시작 화면</button></div></div></div>
</div>
<script type="module">
const $=id=>document.getElementById(id);
let loading=true;const timeout=setTimeout(()=>{if(loading)$('load').innerHTML='<div class="error">3D 엔진 연결이 지연되고 있어요.<br>인터넷 연결·콘텐츠 차단 설정을 확인하고 새로고침해 주세요.</div>'},18000);
try {
const THREE=await import('https://cdn.jsdelivr.net/npm/three@0.170.0/build/three.module.js');
const root=$('game');
const scene=new THREE.Scene();scene.background=new THREE.Color('#9ddded');scene.fog=new THREE.Fog('#b4e3ed',130,420);
const renderer=new THREE.WebGLRenderer({antialias:true,alpha:false,powerPreference:'high-performance'});renderer.setPixelRatio(Math.min(devicePixelRatio,1.5));renderer.shadowMap.enabled=true;renderer.shadowMap.type=THREE.PCFSoftShadowMap;renderer.outputColorSpace=THREE.SRGBColorSpace;root.prepend(renderer.domElement);
const camera=new THREE.PerspectiveCamera(65,1,.2,700);
scene.add(new THREE.HemisphereLight(0xd9faff,0x516c43,2.5));
const sun=new THREE.DirectionalLight(0xfff7df,2.8);sun.position.set(60,110,40);sun.castShadow=true;sun.shadow.mapSize.set(1024,1024);Object.assign(sun.shadow.camera,{left:-160,right:160,top:160,bottom:-160,far:320});scene.add(sun);
const mat=(color,extra={})=>new THREE.MeshStandardMaterial({color,roughness:.78,...extra});
const roadMat=mat('#384b63'),grass=mat('#72bb91'),sand=mat('#f0db9c'),white=mat('#f8ffed'),mint=mat('#b8ffb0'),pink=mat('#fb9ba8'),purple=mat('#bba5f5');
function mesh(g,m,x=0,y=0,z=0,parent=scene){const o=new THREE.Mesh(g,m);o.position.set(x,y,z);parent.add(o);return o}
mesh(new THREE.PlaneGeometry(2200,2200),mat('#58b7d6'),0,-2).rotation.x=-Math.PI/2;
mesh(new THREE.CylinderGeometry(165,180,4,90),sand,0,-1.5).scale.z=.86;
mesh(new THREE.CylinderGeometry(148,164,3,90),grass,0,-.5).scale.z=.86;
const points=[[-98,0,-35],[-76,0,-95],[-8,0,-111],[70,0,-89],[109,0,-34],[79,0,12],[100,0,70],[30,0,101],[-39,0,88],[-101,0,48]].map(p=>new THREE.Vector3(...p));
const curve=new THREE.CatmullRomCurve3(points,true,'centripetal');const LENGTH=curve.getLength(),WIDTH=14,N=900;
const frames=[];
for(let i=0;i<=N;i++){let t=i/N,c=curve.getPointAt(t===1?0:t),v=curve.getTangentAt(t===1?0:t).normalize();frames.push({c,v,r:new THREE.Vector3(v.z,0,-v.x)});}
function frame(distance){let u=((distance%LENGTH)+LENGTH)%LENGTH/LENGTH*N;let i=Math.floor(u),f=u-i,a=frames[i],b=frames[i+1];return {c:a.c.clone().lerp(b.c,f),v:a.v.clone().lerp(b.v,f).normalize(),r:a.r.clone().lerp(b.r,f).normalize()}}
function point(distance,offset=0,y=0){const f=frame(distance);return f.c.addScaledVector(f.r,offset).add(new THREE.Vector3(0,y,0))}
function ribbon(left,right,material,height){let vertices=[],indices=[];for(let i=0;i<=N;i++){for(const d of [left,right]){let p=frames[i].c.clone().addScaledVector(frames[i].r,d);vertices.push(p.x,height,p.z)}if(i<N){let j=i*2;indices.push(j,j+1,j+2,j+1,j+3,j+2)}}const g=new THREE.BufferGeometry();g.setAttribute('position',new THREE.Float32BufferAttribute(vertices,3));g.setIndex(indices);g.computeVertexNormals();const o=new THREE.Mesh(g,material);o.material.side=THREE.DoubleSide;o.receiveShadow=true;scene.add(o)}
ribbon(-WIDTH/2,WIDTH/2,roadMat,.12);ribbon(-8,-7,mint,.14);ribbon(7,8,pink,.14);
for(let s=0;s<LENGTH;s+=9){const f=frame(s);const dash=mesh(new THREE.BoxGeometry(.12,.03,3),white);dash.position.copy(point(s,0,.15));dash.rotation.y=Math.atan2(f.v.x,f.v.z)}
// Small handmade geometric scenery; no copied models or artwork.
function tree(x,z,k){let g=new THREE.Group();scene.add(g);g.position.set(x,0,z);mesh(new THREE.CylinderGeometry(.45,.65,3,6),mat('#86664e'),0,1.5,0,g);let crown=mesh(new THREE.IcosahedronGeometry(3,0),k%2?mat('#428973'):mat('#53a86f'),0,5,0,g);crown.scale.y=1.3}
for(let i=0;i<80;i++){let a=i*2.39996,r=30+((i*29)%90),x=Math.cos(a)*r,z=Math.sin(a)*r*.8;let near=frames.some((f,j)=>j%10===0&&Math.hypot(f.c.x-x,f.c.z-z)<15);if(!near)tree(x,z,i)}
for(let i=0;i<22;i++){const s=i*LENGTH/22;const f=frame(s);for(const side of [-1,1]){const p=point(s,side*10,1.2);const post=mesh(new THREE.CylinderGeometry(.12,.12,2.4,5),white);post.position.copy(p);const flag=mesh(new THREE.BoxGeometry(1.6,1,.07),side>0?pink:mint);flag.position.copy(p).add(new THREE.Vector3(.65,.6,0));flag.rotation.y=Math.atan2(f.v.x,f.v.z)}}
const startF=frame(0),gate=new THREE.Group();gate.position.copy(startF.c);gate.rotation.y=Math.atan2(startF.v.x,startF.v.z);scene.add(gate);
mesh(new THREE.BoxGeometry(.65,8,.65),mint,-8,4,0,gate);mesh(new THREE.BoxGeometry(.65,8,.65),pink,8,4,0,gate);mesh(new THREE.BoxGeometry(16.7,1.5,.65),purple,0,8,0,gate);
for(let x=0;x<14;x++)for(let z=0;z<2;z++)mesh(new THREE.BoxGeometry(1,.04,1),(x+z)%2?roadMat:white,x-6.5,.18,z-.5,gate);
const sparkMat=new THREE.MeshBasicMaterial({color:0xcaff96});
function kart(color){const g=new THREE.Group();scene.add(g);const body=mesh(new THREE.BoxGeometry(1.65,.55,2.45),mat(color),0,.7,0,g);body.castShadow=true;mesh(new THREE.BoxGeometry(1.95,.2,.35),white,0,.45,1.35,g);mesh(new THREE.BoxGeometry(1.95,.2,.35),mat(color),0,.95,-1.2,g);mesh(new THREE.BoxGeometry(1,.38,1.05),mat('#24354b'),0,1.05,-.1,g);mesh(new THREE.SphereGeometry(.49,12,8),mat('#ffe6c4'),0,1.65,-.05,g);mesh(new THREE.SphereGeometry(.53,12,8,0,Math.PI*2,0,Math.PI/2),mat(color),0,1.72,-.05,g);mesh(new THREE.BoxGeometry(.64,.16,.09),mat('#15314b'),0,1.77,.4,g);let stem=mesh(new THREE.CylinderGeometry(.055,.055,.45,5),mat('#467d45'),0,2.24,-.05,g);let leaf=mesh(new THREE.SphereGeometry(.23,8,5),mint,.18,2.4,-.05,g);leaf.scale.set(1.5,.35,.8);const wheels=[];for(const x of [-.95,.95])for(const z of [-.82,.82]){let w=mesh(new THREE.CylinderGeometry(.38,.38,.27,10),mat('#1b263b'),x,.38,z,g);w.rotation.z=Math.PI/2;w.castShadow=true;wheels.push(w)}let shield=mesh(new THREE.SphereGeometry(1.8,16,10),new THREE.MeshBasicMaterial({color:0x81e9ff,transparent:true,opacity:.22,wireframe:true}),0,1,0,g);shield.visible=false;const sparks=[];for(const x of [-.8,.8]){const s=mesh(new THREE.SphereGeometry(.2,5,4),sparkMat,x,.4,-1.4,g);s.visible=false;sparks.push(s)}return {g,wheels,shield,sparks}}
const racers=[{name:'나 · 새싹',color:'#c5fa7e',lane:-2,skill:1},{name:'코랄',color:'#ff9aaf',lane:2,skill:.96},{name:'루모',color:'#b5a3ff',lane:-2,skill:1.025},{name:'모카',color:'#ffc176',lane:2,skill:.99}].map((r,i)=>({...r,visual:kart(r.color),s:-(i<2?5:10),d:r.lane,speed:0,index:i,finish:null,shield:0,slow:0,hitCD:0,lastLap:0,laps:[],bestLap:0,spin:0}));
const player=racers[0];let state='menu',previous='race',countdown=3.5,elapsed=0,boost=25,boosting=false,drift=0,item=null,toastUntil=0,toastText='',useLatch=false,quality=false;
const keys=new Set();let obstacles=[];const pickupGeometry=new THREE.OctahedronGeometry(.8),pickupMaterial=mat('#ffdb7c',{emissive:'#7b4a13',emissiveIntensity:.4});
const pickups=[];for(let s=55;s<LENGTH;s+=75){for(const d of [-3.6,3.6]){const box=mesh(pickupGeometry,pickupMaterial);box.position.copy(point(s,d,1.4));pickups.push({s,d,box,ready:0})}}
let storedBest=null;try{const b=Number(localStorage.getItem('sprout-kart-best-v1'));if(Number.isFinite(b)&&b>0)storedBest=b}catch{}
function fmt(t){if(t==null)return '—';const ms=Math.floor(Math.max(0,t)*1000);return String(Math.floor(ms/60000)).padStart(2,'0')+':'+String(Math.floor(ms/1000)%60).padStart(2,'0')+'.'+String(ms%1000).padStart(3,'0')}
function showBest(){$('best').textContent=storedBest?'이 브라우저 최고 기록 · '+fmt(storedBest):'나만의 첫 완주 기록을 남겨 보세요. 기록은 이 브라우저에만 저장됩니다.'}showBest();
function toast(text,sec=2){toastText=text;toastUntil=elapsed+sec;$('toast').textContent=text}
function reset(){for(const r of racers){r.s=-(r.index<2?5:10);r.d=r.lane;r.speed=0;r.finish=null;r.shield=0;r.slow=0;r.hitCD=0;r.lastLap=0;r.laps=[];r.spin=0}for(const p of pickups){p.ready=0;p.box.visible=true}for(const o of obstacles)scene.remove(o.mesh);obstacles=[];elapsed=0;countdown=3.5;boost=25;drift=0;item=null;toastUntil=0;keys.clear();useLatch=false;state='countdown';$('start').classList.add('hidden');$('result').classList.add('hidden');$('paused').classList.add('hidden');$('pause').textContent='일시정지';$('toast').textContent='';root.focus();positionRacers(0)}
function pause(){if(state==='race'||state==='countdown'){previous=state;state='paused';keys.clear();document.querySelectorAll('.pressed').forEach(b=>b.classList.remove('pressed'));$('paused').classList.remove('hidden')}}
function resume(){if(state==='paused'){state=previous;$('paused').classList.add('hidden');keys.clear();root.focus()}}
$('startBtn').onclick=reset;$('again').onclick=reset;$('restartPause').onclick=reset;$('resume').onclick=resume;$('pause').onclick=()=>state==='paused'?resume():pause();$('home').onclick=()=>{state='menu';$('result').classList.add('hidden');$('start').classList.remove('hidden');showBest()};
$('quality').onclick=()=>{quality=!quality;renderer.setPixelRatio(Math.min(devicePixelRatio,quality?2:1));renderer.shadowMap.enabled=quality;resize();$('quality').textContent='화질: '+(quality?'높음':'절전')};
$('full').onclick=async()=>{try{if(document.fullscreenElement)await document.exitFullscreen();else await root.requestFullscreen()}catch{toast('이 브라우저에서는 전체화면을 지원하지 않습니다.')}};
const handled=['ArrowLeft','ArrowRight','ArrowUp','ArrowDown','Space','ShiftLeft','ShiftRight','KeyE','Escape'];
root.addEventListener('keydown',e=>{if(handled.includes(e.code)){e.preventDefault();if(e.code==='Escape'){if(!e.repeat)(state==='paused'?resume():pause());return}keys.add(e.code)}});root.addEventListener('keyup',e=>{keys.delete(e.code);if(handled.includes(e.code))e.preventDefault()});
root.addEventListener('pointerdown',e=>{if(e.target.tagName==='CANVAS')root.focus()});
window.addEventListener('blur',()=>{keys.clear();pause()});document.addEventListener('visibilitychange',()=>{if(document.hidden)pause()});
for(const b of document.querySelectorAll('[data-key]')){const pointers=new Set();b.addEventListener('pointerdown',e=>{e.preventDefault();b.setPointerCapture(e.pointerId);pointers.add(e.pointerId);keys.add(b.dataset.key);b.classList.add('pressed');root.focus()});const end=e=>{pointers.delete(e.pointerId);if(!pointers.size){keys.delete(b.dataset.key);b.classList.remove('pressed')}};b.addEventListener('pointerup',end);b.addEventListener('pointercancel',end);b.addEventListener('lostpointercapture',end)}
function wrappedDistance(a,b){let d=(a-b)%LENGTH;if(d>LENGTH/2)d-=LENGTH;if(d<-LENGTH/2)d+=LENGTH;return d}
function rankings(){return [...racers].sort((a,b)=>{if(a.finish!=null&&b.finish!=null)return a.finish-b.finish;if(a.finish!=null)return -1;if(b.finish!=null)return 1;return b.s-a.s})}
function useItem(){if(!item)return;const used=item;item=null;if(used==='부스터'){boost=Math.min(100,boost+45);toast('⚡ 부스터 +45%')}if(used==='보호막'){player.shield=7;toast('🛡️ 7초 보호막')}if(used==='씨앗 덫'){const p=point(player.s-4,player.d,.4);const o=mesh(new THREE.IcosahedronGeometry(.65,0),pink);o.position.copy(p);obstacles.push({s:player.s-4,d:player.d,mesh:o,until:elapsed+16});toast('🌰 뒤에 씨앗 덫 설치!')}if(used==='민트 파동'){let hit=false;for(const r of racers.slice(1)){const d=wrappedDistance(r.s,player.s);if(d>0&&d<34&&Math.abs(r.d-player.d)<6&&r.finish===null){if(r.shield<=0){r.slow=2.6;r.spin=.5;hit=true}}}toast(hit?'🌀 앞쪽 상대에게 민트 파동!':'🌀 사정거리 안에 상대가 없어요')}}
function hit(r,slow=1.7){if(r.shield>0||r.hitCD>0)return;r.slow=Math.max(r.slow,slow);r.speed*=.65;r.hitCD=1.4;r.spin=.5;if(r===player)toast('잠깐 미끄러졌어요! 다시 가속하세요.')}
function step(dt){if(state==='countdown'){countdown-=dt;$('count').textContent=countdown>0?String(Math.ceil(countdown)):'GO!';if(countdown<=-.65){state='race';$('count').textContent='';toast('아이템 상자를 모으고 부스터를 충전하세요!',3)}return}
if(state!=='race')return;elapsed+=dt;boosting=false;
for(const r of racers){if(r.finish!==null)continue;r.shield=Math.max(0,r.shield-dt);r.slow=Math.max(0,r.slow-dt);r.hitCD=Math.max(0,r.hitCD-dt);r.spin=Math.max(0,r.spin-dt);let target=0;
if(r===player){let steer=(keys.has('ArrowRight')?1:0)-(keys.has('ArrowLeft')?1:0);let active=keys.has('Space')&&Math.abs(steer)>0&&r.speed>12;let offroad=Math.abs(r.d)>WIDTH/2-.2;boosting=(keys.has('ShiftLeft')||keys.has('ShiftRight'))&&boost>0&&r.speed>5;
if(boosting)boost=Math.max(0,boost-29*dt);else boost=Math.min(100,boost+dt*(active?15:3));
if(active){drift+=dt}else if(drift>.6){boost=Math.min(100,boost+Math.min(18,drift*5));toast('드리프트 충전!');drift=0}else drift=0;
r.d+=steer*(active?5.4:7.3)*dt*Math.min(1,r.speed/12);r.d=Math.max(-10,Math.min(10,r.d));
target=keys.has('ArrowUp')?(boosting?53:37):0;if(keys.has('ArrowDown'))target=0;if(offroad)target=Math.min(target,17);if(r.slow>0)target=Math.min(target,12);r.speed+=(target-r.speed)*Math.min(1,dt*(keys.has('ArrowDown')?4.5:target>r.speed?1.0:.7));
if(keys.has('KeyE')&&!useLatch)useItem();useLatch=keys.has('KeyE');
}else{r.d+=(r.lane+Math.sin(elapsed*.8+r.index)*1.9-r.d)*dt*.8;target=33*r.skill+Math.sin(elapsed*.65+r.index)*2.5;if(r.slow>0)target=12;r.speed+=(target-r.speed)*Math.min(1,dt*.9);}
const old=r.s;r.s+=Math.max(0,r.speed)*dt;
// Race progress is monotonically integrated; no teleport shortcuts or reverse-lap exploits.
const oldLap=Math.max(0,Math.floor(old/LENGTH)),newLap=Math.max(0,Math.floor(r.s/LENGTH));
if(newLap>oldLap){const fraction=(newLap*LENGTH-old)/Math.max(.00001,r.s-old);const crossing=elapsed-dt+fraction*dt;r.laps.push(crossing-r.lastLap);r.lastLap=crossing;if(newLap>=3){r.finish=crossing;r.s=3*LENGTH;r.speed=0}else if(r===player){toast('🏁 '+newLap+'바퀴 완료! '+fmt(r.laps.at(-1)),3)}}
}
// Position and longitudinal distance are both needed for collisions.
for(let i=0;i<racers.length;i++)for(let j=i+1;j<racers.length;j++){const a=racers[i],b=racers[j];if(a.finish!=null||b.finish!=null)continue;if(Math.abs(wrappedDistance(a.s,b.s))<2.4&&Math.abs(a.d-b.d)<1.8){const side=a.d>=b.d?1:-1;a.d=Math.max(-10,Math.min(10,a.d+side*dt*3));b.d=Math.max(-10,Math.min(10,b.d-side*dt*3));if(a.hitCD<=0&&b.hitCD<=0){a.speed*=.86;b.speed*=.86;a.hitCD=b.hitCD=.8}}}
for(const p of pickups){p.box.visible=elapsed>=p.ready;if(!p.box.visible)continue;for(const r of racers){if(r.finish!=null)continue;if(Math.abs(wrappedDistance(r.s,p.s))<2&&Math.abs(r.d-p.d)<1.7){if(r===player&&!item){const items=['부스터','보호막','씨앗 덫','민트 파동'];item=items[Math.floor(Math.random()*items.length)];p.ready=elapsed+7;toast('🎁 '+item+' 획득! E 또는 아이템 버튼')}else if(r!==player){p.ready=elapsed+7;r.shield=1.5}break}}}
for(const o of obstacles){for(const r of racers){if(r.finish===null&&Math.abs(wrappedDistance(r.s,o.s))<1.8&&Math.abs(r.d-o.d)<1.5){hit(r,2.1);o.until=0;break}}}
obstacles=obstacles.filter(o=>{if(elapsed>o.until){scene.remove(o.mesh);return false}return true});
if(player.finish!==null)finishRace();
}
function finishRace(){state='finished';keys.clear();let order=rankings(),rank=order.indexOf(player)+1;let newBest=storedBest===null||player.finish<storedBest;if(newBest){storedBest=player.finish;try{localStorage.setItem('sprout-kart-best-v1',String(storedBest))}catch{}}$('resultTitle').textContent=rank===1?'우승! 🌿':rank+'위 완주!';$('resultTime').textContent=fmt(player.finish)+(newBest?' · 나의 신기록!':'');const table=document.createElement('table');for(let i=0;i<order.length;i++){const r=order[i],tr=document.createElement('tr');for(const v of [String(i+1)+'위',r.name,r.finish!==null?fmt(r.finish):'진행 중 · '+(Math.min(100,r.s/(3*LENGTH)*100)).toFixed(1)+'%']){const td=document.createElement('td');td.textContent=v;tr.appendChild(td)}table.appendChild(tr)}$('resultTable').replaceChildren(table);$('resultLaps').textContent=player.laps.map((t,i)=>(i+1)+'랩 '+fmt(t)).join(' / ');$('result').classList.remove('hidden');$('count').textContent='';showBest()}
function positionRacers(dt){for(const r of racers){const f=frame(r.s);r.visual.g.position.copy(point(r.s,r.d,.15));let steer=r===player?((keys.has('ArrowRight')?1:0)-(keys.has('ArrowLeft')?1:0)):0;let driftAngle=r===player&&keys.has('Space')&&r.speed>12?steer*.34:0;r.visual.g.rotation.y=Math.atan2(f.v.x,f.v.z)+driftAngle+Math.sin(r.spin*20)*r.spin*.8;r.visual.g.rotation.z=-steer*.05;r.visual.shield.visible=r.shield>0;for(const w of r.visual.wheels)w.rotation.x+=r.speed*dt*2;for(const s of r.visual.sparks)s.visible=r===player&&((drift>.4)||(boosting&&state==='race'));}}
let hudTimer=0;
function hud(dt){hudTimer+=dt;if(hudTimer<.07)return;hudTimer=0;const order=rankings();$('rank').textContent=order.indexOf(player)+1;$('lap').textContent=Math.min(3,Math.max(1,Math.floor(Math.max(0,player.s)/LENGTH)+1))+' / 3';$('time').textContent=fmt(player.finish??elapsed);$('speed').innerHTML=Math.round(player.speed*3.6)+' <small style="font-size:11px">km/h</small>';$('boostval').textContent=Math.floor(boost);$('boostbar').style.width=boost+'%';$('item').textContent=item?'🎁 '+item:'아이템 없음';$('laps').textContent=player.laps.map((v,i)=>(i+1)+'L '+fmt(v)).join(' · ');$('leader').textContent='';for(const [i,r] of order.entries()){const d=document.createElement('div');d.textContent=(i+1)+'. '+r.name+(r.finish!==null?' 🏁':'');d.style.color=r===player?'#d2ff87':'#e4edf4';$('leader').appendChild(d)}if(state==='race')$('toast').textContent=elapsed<toastUntil?toastText:'';}
function resize(){const w=Math.max(320,root.clientWidth),h=root.clientHeight;renderer.setSize(w,h,false);camera.aspect=w/h;camera.updateProjectionMatrix()}new ResizeObserver(resize).observe(root);resize();
let last=performance.now();positionRacers(0);let initF=frame(player.s);camera.position.copy(point(player.s-14,player.d,8));camera.lookAt(point(player.s+14,0,1));
function animate(now){requestAnimationFrame(animate);let dt=Math.min(.05,Math.max(0,(now-last)/1000));last=now;step(dt);positionRacers(dt);const p=frame(player.s);let cp=point(player.s-12,player.d*.7,6.7);camera.position.lerp(cp,1-Math.exp(-dt*6));camera.lookAt(point(player.s+13,player.d*.3,1.3));for(const box of pickups){box.box.rotation.y+=dt*1.6;box.box.position.y=1.4+Math.sin(now*.002+box.s)*.22}hud(dt);renderer.render(scene,camera)}
loading=false;clearTimeout(timeout);$('load').classList.add('hidden');requestAnimationFrame(animate);
} catch(error) {loading=false;clearTimeout(timeout);$('load').innerHTML='<div class="error"><h2>3D 게임을 시작하지 못했어요.</h2>인터넷 연결과 브라우저의 하드웨어 가속/WebGL 설정을 확인해 주세요.<br>최신 Chrome·Edge·Safari에서 다시 시도해 주세요.<p id="errdetail" style="font-size:12px"></p></div>';$('errdetail').textContent=String(error.message||error);console.error(error)}
</script></body></html>'''
components.html(GAME, height=790, scrolling=False)
with st.expander('조작 방법 · 배포 안내'):
    st.markdown('''**PC:** 게임 화면을 클릭한 후 ↑ 가속 / ↓ 감속 / ← → 조향 / Space 드리프트 / Shift 부스터 / E 아이템.  
**모바일:** 화면 아래 터치 버튼을 동시에 누르세요. 가로 화면·전체화면을 권장합니다.

- 트랙 1개, AI 3대, 3바퀴 경기입니다. 코스 진행 방향이 자동 보조되는 아케이드 방식입니다.
- 가속 버튼을 눌러야 출발합니다. 트랙 밖으로 벗어나면 속도가 줄어듭니다.
- 드리프트와 주행으로 부스터를 충전하고 Shift로 사용합니다. 상자에서 보조 아이템을 얻습니다.
- 탭 이동·창 포커스 이탈 시 자동 일시정지됩니다. 돌아오면 ‘계속 달리기’를 누르세요.
- 최고 완주 기록은 해당 브라우저에만 저장됩니다. 브라우저 저장 차단 시 기록 저장이 안 될 수 있습니다.
- **배포:** 두 파일을 GitHub에 올리고 Streamlit Cloud의 실행 경로를 `app.py`로 지정하세요. API 키는 필요 없습니다.
- 브라우저에서 외부 CDN의 Three.js를 불러오므로 인터넷·WebGL이 필요합니다. 오프라인 실행·실시간 멀티플레이·사운드는 포함하지 않았습니다.
- 완주 시 이미 완주한 AI는 기록 순으로, 아직 주행 중인 AI는 진행 거리 순으로 표시합니다.
''')
