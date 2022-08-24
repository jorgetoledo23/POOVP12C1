public class Encomienda{
    //Atributos
    string Remitente;
    string Destinatario;
    double Peso;
    int ValorEnvio;
    int dimensiones;
}

public class JefeSucursal{
    public string Rut { get; set; }
    public string Nombre { get; set; }
    public string Apellido { get; set; }
}
public class Sucursal{
    public string Ciudad { get; set; }
    public string Direccion { get; set; }
    public JefeSucursal Jefe {get; set;}

}