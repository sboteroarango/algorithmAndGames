
public static void main(String[] args)
{
  float valorapagar=760F;
  float valorpagado;
  if (valorapagar>30F)
  {
    if((valorapagar>500F)&&(valorapagar<700F))
    {
      System.out.println("Subtotal: "+valorapagar+" USD");
      valorpagado=valorapagar-(valorapagar*(15F/100F));
      System.out.println("Descuento: "+(valorapagar-valorpagado)+" USD");
      System.out.println("Impuesto: "+(valorpagado*(8F/100F))+" USD");
      valorpagado=valorpagado+(valorpagado*(8F/100F));
      System.out.println("Total: "+(valorpagado)+" USD");
    }
    if((valorapagar>700F)&&(valorapagar<1250F))
    {
      System.out.println("Subtotal: "+valorapagar+" USD");
      valorpagado=valorapagar-(valorapagar*(25F/100F));
      System.out.println("Descuento: "+(valorapagar-valorpagado)+" USD");
      System.out.println("Impuesto: "+(valorpagado*(8F/100F))+" USD");
      valorpagado=valorpagado+(valorpagado*(8F/100F));
      System.out.println("Total: "+(valorpagado)+" USD");
    }
  }
  else
  {
    System.out.println("Subtotal: "+valorapagar+" USD");
    System.out.println("Descuento: "+0F+" USD");
    System.out.println("Impuesto: "+0F+" USD");
    System.out.println("Total: "+valorapagar+" USD");
            }
}
