function submit() {
  let form = document.getElementById("form");
  form.submit();
  alert("Data stored in database!");
}


let width = 281;
let height = 180;

let stage = new Konva.Stage({
    container: 'container1',
    width: width,
    height: height,
});

let layer1 = new Konva.Layer();
let layer2 = new Konva.Layer();
let imageObj = new Image();
  imageObj.onload = function () {
      let yoda = new Konva.Image({
          x: 0,
          y: 0,
          image: imageObj,
          width: stage.width(),
          height: stage.height(),
      });
      // add the shape to the layer
      layer1.add(yoda);
  };

  console.log(path);
  imageObj.src = path;

let rect = new Konva.Rect({
    x: 0,
    y: 0,
    width: 150,
    height: 90,
    fill: 'blue',
    name: 'rect',
    draggable: true,
    opacity: 0.1,
});

layer2.add(rect);

stage.add(layer1);
stage.add(layer2);

let tr = new Konva.Transformer();
layer2.add(tr);

// by default select all shapes
tr.nodes([ rect]);

// add a new feature, lets add ability to draw selection rectangle
let selectionRectangle = new Konva.Rect({
  fill: 'rgba(0,0,255,0.5)',
  visible: false,
});
layer1.add(selectionRectangle);

let x1, y1, x2, y2;
stage.on('mousedown touchstart', (e) => {
  // do nothing if we mousedown on any shape
  if (e.target !== stage) {
    return;
  }
  e.evt.preventDefault();
  x1 = stage.getPointerPosition().x;
  y1 = stage.getPointerPosition().y;
  x2 = stage.getPointerPosition().x;
  y2 = stage.getPointerPosition().y;

  selectionRectangle.visible(true);
  selectionRectangle.width(0);
  selectionRectangle.height(0);
});

stage.on('mousemove touchmove', (e) => {
  // do nothing if we didn't start selection
  if (!selectionRectangle.visible()) {
    return;
  }
  e.evt.preventDefault();
  x2 = stage.getPointerPosition().x;
  y2 = stage.getPointerPosition().y;

  selectionRectangle.setAttrs({
    x: Math.min(x1, x2),
    y: Math.min(y1, y2),
    width: Math.abs(x2 - x1),
    height: Math.abs(y2 - y1),
  });
});

stage.on('mouseup touchend', (e) => {
  // do nothing if we didn't start selection
  if (!selectionRectangle.visible()) {
    return;
  }
  e.evt.preventDefault();
  // update visibility in timeout, so we can check it in click event
  setTimeout(() => {
    selectionRectangle.visible(false);
  });

  let shapes = stage.find('.rect');
  let box = selectionRectangle.getClientRect();
  let selected = shapes.filter((shape) =>
    Konva.Util.haveIntersection(box, shape.getClientRect())
  );
  tr.nodes(selected);
});

// clicks should select/deselect shapes
stage.on('click tap', function (e) {
  // if we are selecting with rect, do nothing
  if (selectionRectangle.visible()) {
    return;
  }

  // if click on empty area - remove all selections
  if (e.target === stage) {
    tr.nodes([]);
    return;
  }

  // do nothing if clicked NOT on our rectangles
  if (!e.target.hasName('rect')) {
    return;
  }

  // do we pressed shift or ctrl?
  const metaPressed = e.evt.shiftKey || e.evt.ctrlKey || e.evt.metaKey;
  const isSelected = tr.nodes().indexOf(e.target) >= 0;

  if (!metaPressed && !isSelected) {
    // if no key pressed and the node is not selected
    // select just one
    tr.nodes([e.target]);
  } else if (metaPressed && isSelected) {
    // if we pressed keys and node was selected
    // we need to remove it from selection:
    const nodes = tr.nodes().slice(); // use slice to have new copy of array
    // remove node from array
    nodes.splice(nodes.indexOf(e.target), 1);
    tr.nodes(nodes);
  } else if (metaPressed && !isSelected) {
    // add the node into selection
    const nodes = tr.nodes().concat([e.target]);
    tr.nodes(nodes);
  }

});


let width2 = 281;
let height2 = 180;

let stage2 = new Konva.Stage({
    container: 'container2',
    width: width2,
    height: height2,
});

let layer3 = new Konva.Layer();
let layer4 = new Konva.Layer();
let imageObj2 = new Image();
  imageObj2.onload = function () {
      let yoda = new Konva.Image({
          x: 0,
          y: 0,
          image: imageObj2,
          width: stage.width(),
          height: stage.height(),
      });

      // add the shape to the layer
      layer3.add(yoda);
  };
  console.log(path2);
  imageObj2.src = path2;

let rect1 = new Konva.Rect({
    x: 0,
    y: 0,
    width: 150,
    height: 90,
    fill: 'blue',
    name: 'rect1',
    draggable: true,
    opacity: 0.1,
});

layer4.add(rect1);

stage2.add(layer3);
stage2.add(layer4);

let tr1 = new Konva.Transformer();
layer4.add(tr1);

// by default select all shapes
tr1.nodes([ rect1]);

// add a new feature, lets add ability to draw selection rectangle
let selectionRectangle1 = new Konva.Rect({
  fill: 'rgba(0,0,255,0.5)',
  visible: false,
});
layer3.add(selectionRectangle1);

let x3, y3, x4, y4;
var ajk= null;
stage2.on('mousedown touchstart', (e) => {
  // do nothing if we mousedown on any shape
  if (e.target !== stage2) {
    return;
  }
  e.evt.preventDefault();
  x3 = stage2.getPointerPosition().x;
  y3 = stage2.getPointerPosition().y;
  x4 = stage2.getPointerPosition().x;
  y4 = stage2.getPointerPosition().y;

  selectionRectangle1.visible(true);
  selectionRectangle1.width(0);
  selectionRectangle1.height(0);
});

// console.log(rect1.x);
stage2.on('mousemove touchmove', (e) => {
  // do nothing if we didn't start selection
  if (!selectionRectangle1.visible()) {
    return;
  }
  e.evt.preventDefault();
  x4 = stage2.getPointerPosition().x;
  y4 = stage2.getPointerPosition().y;

  selectionRectangle1.setAttrs({
    x: Math.min(x3, x4),
    y: Math.min(y3, y4),
    width: Math.abs(x4 - x3),
    height: Math.abs(y4 - y3),
  });
});

stage2.on('mouseup touchend', (e) => {
  // do nothing if we didn't start selection
  if (!selectionRectangle1.visible()) {
    return;
  }
  e.evt.preventDefault();
  // update visibility in timeout, so we can check it in click event
  setTimeout(() => {
    selectionRectangle1.visible(false);
  });

  let shapes1 = stage2.find('.rect1');
  let box1 = selectionRectangle1.getClientRect();
  let selected1 = shapes1.filter((shape) =>
    Konva.Util.haveIntersection(box1, shape.getClientRect())
  );
  tr1.nodes(selected1);
});

// clicks should select/deselect shapes
stage2.on('click tap', function (e) {
  // if we are selecting with rect, do nothing
  if (selectionRectangle1.visible()) {
    return;
  }

  // if click on empty area - remove all selections
  if (e.target === stage2) {
    tr1.nodes([]);
    return;
  }

  // do nothing if clicked NOT on our rectangles
  if (!e.target.hasName('rect1')) {
    return;
  }

  // do we pressed shift or ctrl?
  const metaPressed1 = e.evt.shiftKey || e.evt.ctrlKey || e.evt.metaKey;
  const isSelected1 = tr1.nodes().indexOf(e.target) >= 0;

  if (!metaPressed1 && !isSelected1) {
    // if no key pressed and the node is not selected
    // select just one
    tr1.nodes([e.target]);
  } else if (metaPressed1 && isSelected1) {
    // if we pressed keys and node was selected
    // we need to remove it from selection:
    const nodes = tr1.nodes().slice(); // use slice to have new copy of array
    // remove node from array
    nodes.splice(nodes.indexOf(e.target), 1);
    tr1.nodes(nodes);
  } else if (metaPressed1 && !isSelected1) {
    // add the node into selection
    const nodes = tr1.nodes().concat([e.target]);
    tr1.nodes(nodes);
  }
});

let zorar = document.getElementById('zorar');
zorar.onclick = __=>{


  console.log(`
   Width: ${rect1.width()}
   Height: ${rect1.height()}
   ScaleX: ${rect1.scaleX()}
   ScaleY: ${rect1.scaleY()}

   New Width: ${rect1.width() * rect1.scaleX()}
   New Height: ${rect1.height() * rect1.scaleY()}

  Width0: ${rect.width()}
  Height0: ${rect.height()}
  ScaleX0: ${rect.scaleX()}
  ScaleY0: ${rect.scaleY()}

  New Width0: ${rect.width() * rect.scaleX()}
  New Height0: ${rect.height() * rect.scaleY()}
  `)
  
  $.ajax({
    method: 'POST',
    url: 'http://127.0.0.1:5000/getC',
    dataType: 'json',
    async: false,
    data: {
        x1: rect.attrs.x,
        y1: rect.attrs.y,
        w1: rect.width() * rect.scaleX(),
        h1: rect.width() * rect.scaleX(),
        x2: rect1.attrs.x,
        y2: rect1.attrs.y,
        w2: rect1.width() * rect1.scaleX(),
        h2: rect1.height() * rect1.scaleY(),
    },
    success: function (res, status, xhr) {
        console.log(res);
    }
});
}
