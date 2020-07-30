function hslToRgb(h, s, l) {
    var r, g, b;

     if (s == 0) {
         r = g = b = l; // achromatic
     } else {
         function hue2rgb(p, q, t) {
             if (t < 0) t += 1;
             if (t > 1) t -= 1;
             if (t < 1 / 6) return p + (q - p) * 6 * t;
             if (t < 1 / 2) return q;
             if (t < 2 / 3) return p + (q - p) * (2 / 3 - t) * 6;
             return p;
         }

         var q = l < 0.5 ? l * (1 + s) : l + s - l * s;
         var p = 2 * l - q;
         r = hue2rgb(p, q, h + 1 / 3);
         g = hue2rgb(p, q, h);
         b = hue2rgb(p, q, h - 1 / 3);
     }
     return [r * 255, g * 255, b * 255];
 }

 function ColorGroupInitialize(){
   let t_colorgroup={};
   t_colorgroup['line1']=[getRandomInt(255), getRandomInt(255), getRandomInt(255)];
   t_colorgroup['line2']=[getRandomInt(255), getRandomInt(255), getRandomInt(255)];

   t_colorgroup['drone1']=[getRandomInt(255), getRandomInt(255), getRandomInt(255)];
   t_colorgroup['drone2']=[getRandomInt(255), getRandomInt(255), getRandomInt(255)];

   t_colorgroup['path1']=[getRandomInt(255), getRandomInt(255), getRandomInt(255)];
   t_colorgroup['path2']=[getRandomInt(255), getRandomInt(255), getRandomInt(255)];
   return t_colorgroup;
 }

 function getRandomInt(max) {
   return Math.floor(Math.random() * Math.floor(max));
 }

 function download(filename, text) {
   var element = document.createElement('a');
   element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
   element.setAttribute('download', filename);

   element.style.display = 'none';
   document.body.appendChild(element);

   element.click();

   document.body.removeChild(element);
 }

 function ContourRingdownload(in_rings,index=0){
   // 20200723 tian start test
   // target: use python to generate contour map images
   // download the rings to a document
   console.log(in_rings);
   str_ring=JSON.stringify(in_rings);
   let filename="Ring"+"_"+index.toString()+".txt";
   download(filename, str_ring);
 }

 function polygonClone(polygon) {
   let cloned = [],
       i,
       n;

   for (i = 0, n = polygon.length; i < n; i++) {
     cloned.push([polygon[i][0], polygon[i][1]]);
   }

   return cloned;
 }


function FilterBoundary(x,y,maxx,maxy,minx,miny){
  if (x>maxx) {
   x=maxx;
  }
  else if (x<minx) {
   x=minx;
  }
  if (y>maxy) {
   y=maxy;
  }
  else if (y<miny) {
   y=miny;
  }
  return [x,y];
}


var m_clue_template = {
    title: "{Name}",
    content: [
      {
        type: "fields",
        fieldInfos: [{fieldName: "Name"},{fieldName: "LostHour"}]
      }
    ]
};
