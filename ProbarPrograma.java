public class ProbarPrograma{
    
    public static void main(String args[])
    {
        
        OrdenSelec ordena = new OrdenSelec();
        int [] arreglo = { 70 , 15 , 2 , 456 , 452 , 30 , 20 , 1 , 61 };
        ordena.ordenamientoPorSeleccion(arreglo); 
        ordena.imprime(arreglo);
        
    }
}
