//Tarea 5 Ordenamiento por selección 
//BECERRA ANGELES ROBERTO ALEXIS 
public class OrdenSelec{

    public void ordenamientoPorSeleccion(int arr[])
    {
        for (int pivote = 0; pivote < arr.length - 1; pivote++){
            int min = pivote;
            for (int aux = pivote + 1 ; aux < arr.length; aux++){
                if (arr[aux] < arr[min]){
                    min = aux;

                }
            }
            int temp = arr[pivote];
            arr[pivote]=arr[min];
            arr[min]= temp;
        }
    }
    public void imprime(int arr[]){
        for (int i = 0; i < arr.length ;i++){
            System.out.println(arr[i]);
        }
    }
}
