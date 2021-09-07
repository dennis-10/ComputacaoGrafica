void setup()
{
  size(800,600);
}

void draw()
{
  background(128);
  
  
  float p1x = 100;
  float p1y = 100;

  // Alterando os valores em X para p2, tenho uma curva mais ou menos torta
  float p2x = mouseX - 800;
  float p2y = mouseY;
  
  float p3x = mouseX;
  float p3y = mouseY;
  
  float p4x = 700;
  float p4y = 100;
  
  beginShape();  
  vertex(p1x, p1y);
  
  for(float t = 0; t <= 1; t += 0.01)
  {
    // coordenadas dos pontos gerados nas retas p1p2, p2p3, p3p4 
    float ax = p1x + t*(p2x-p1x);
    float bx = p2x + t*(p3x-p2x);
    float cx = p3x + t*(p4x-p3x);
    
    float ay = p1y + t*(p2y-p1y);
    float by = p2y + t*(p3y-p2y);
    float cy = p3y + t*(p4y-p3y);
    
    // coordenadas dos pontos sobre as retas geradas por axbxbxby e bxbycxcy
    float dx = ax + t*(bx-ax);
    float dy = ay + t*(by-ay);
    
    float ex = bx + t*(cx-bx);
    float ey = by + t*(cy-by);
    
    // definindo o ponto que faz a curva e anda na reta anteriorr
    float fx = dx + t*(ex-dx);
    float fy = dy + t*(ey-dy);
    
    vertex(fx,fy);
    //vertex(bx,by);
    //vertex(cx,cy);
    //vertex(cx,cy);  
  }
  
  vertex(p4x, p4y);
  endShape(CLOSE);
}
