(()=>{"use strict";({590:function(t,e){var o=this&&this.__awaiter||function(t,e,o,n){return new(o||(o=Promise))((function(d,c){function i(t){try{a(n.next(t))}catch(t){c(t)}}function s(t){try{a(n.throw(t))}catch(t){c(t)}}function a(t){var e;t.done?d(t.value):(e=t.value,e instanceof o?e:new o((function(t){t(e)}))).then(i,s)}a((n=n.apply(t,e||[])).next())}))};Object.defineProperty(e,"__esModule",{value:!0}),console.log("Welcome to Add.");let n=new Headers;n.append("Accept","application/json");let d=new FormData;d.append("x","100"),d.append("y","100");const c={task_status:function(t){return o(this,void 0,void 0,(function*(){const e=yield fetch(`http://localhost:8000/da/post-add/${t}/`,{method:"GET",mode:"cors",headers:n});return yield e.json()}))},get_task_id:function(t,e){return o(this,void 0,void 0,(function*(){const t=yield fetch("http://localhost:8000/da/post-add/",{method:"POST",body:d,mode:"cors",headers:n}),e=yield t.text();return JSON.parse(e).id}))}};!function(){o(this,void 0,void 0,(function*(){document.querySelector("#add-box-button").onclick=function(t){return o(this,void 0,void 0,(function*(){document.querySelector("#add-box-a"),document.querySelector("#add-box-b");let t=yield c.get_task_id(100,200);console.log(t);let e=!0,o=null;for(;e;)o=yield c.task_status(t),console.log(o),200===o.result&&(console.log(o),e=!1)}))}}))}()}})[590](0,{})})();