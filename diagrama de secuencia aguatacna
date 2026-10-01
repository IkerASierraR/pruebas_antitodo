# Diagramas de Secuencia del Sistema AguaTacna

Este documento consolida la arquitectura y los **diagramas de secuencia completos** de la aplicación **AguaTacna** (Compose Multiplatform: Android & iOS). Cada módulo está desglosado en sus casos de uso y funciones principales, modelados mediante especificación **Mermaid** y alineados con la arquitectura Clean Architecture, flujo MVI/MVVM reactivo (Coroutines & Flows), Room como única fuente de verdad local (*Single Source of Truth*) y sincronización offline-first con Supabase / n8n.

---

## Tabla de Contenidos

1. [Convenciones de Arquitectura y Actores](#convenciones-de-arquitectura-y-actores)
2. [Módulo 1: Sesión, Onboarding y Bienvenida](#modulo-1-sesion-onboarding-y-bienvenida)
   - [1.1 Verificación de Estado de Sesión y Onboarding (`PuertaDeAcceso`)](#11-verificacion-de-estado-de-sesion-y-onboarding-puertadeacceso)
   - [1.2 Inicio de Sesión Anónimo (`Empezar sin cuenta`)](#12-inicio-de-sesion-anonimo-empezar-sin-cuenta)
   - [1.3 Inicio de Sesión con Google (`InicioConGoogle`)](#13-inicio-de-sesion-con-google-iniciocongoogle)
3. [Módulo 2: Reserva (Gestión Hídrica del Hogar)](#modulo-2-reserva-gestion-hidrica-del-hogar)
   - [2.1 Configuración Inicial del Hogar (`ConfiguracionViewModel`)](#21-configuracion-inicial-del-hogar-configuracionviewmodel)
   - [2.2 Registro de Evento de Llenado (Real vs Confirmación de Asumido)](#22-registro-de-evento-de-llenado-real-vs-confirmacion-de-asumido)
   - [2.3 Monitoreo Reactivo y Proyección Continua de Agotamiento](#23-monitoreo-reactivo-y-proyeccion-continua-de-agotamiento)
   - [2.4 Declaración de Agotamiento Real (`Me quedé sin agua`) y Recalibración](#24-declaracion-de-agotamiento-real-me-quede-sin-agua-y-recalibracion)
   - [2.5 Simulación y Sugerencia de Recortes de Consumo (`¿Qué recortar?`)](#25-simulacion-y-sugerencia-de-recortes-de-consumo-que-recortar)
   - [2.6 Tarea Periódica de Recálculo y Emisión de Avisos Preventivos (Worker)](#26-tarea-periodica-de-recalculo-y-emision-de-avisos-preventivos-worker)
   - [2.7 Sincronización en la Nube con Supabase (`SincronizadorReserva`)](#27-sincronizacion-en-la-nube-con-supabase-sincronizadorreserva)
4. [Módulo 3: Sector y Abastecimiento (Horarios y Cisternas)](#modulo-3-sector-y-abastecimiento-horarios-y-cisternas)
   - [3.1 Detección Espacial y Registro de Domicilio / Sector](#31-deteccion-espacial-y-registro-de-domicilio--sector)
   - [3.2 Consulta de Cronograma Vigente y Próximo Abastecimiento](#32-consulta-de-cronograma-vigente-y-proximo-abastecimiento)
   - [3.3 Confirmación Colaborativa Comunitaria (Llegada / Corte de Agua)](#33-confirmacion-colaborativa-comunitaria-llegada--corte-de-agua)
   - [3.4 Consolidación Algorítmica de Cronograma Colaborativo por Mediana](#34-consolidacion-algoritmica-de-cronograma-colaborativo-por-mediana)
   - [3.5 Búsqueda y Localización Espacial de Puntos de Cisterna](#35-busqueda-y-localizacion-espacial-de-puntos-de-cisterna)
   - [3.6 Sincronización Remota de Sectores y Cronogramas con Supabase](#36-sincronizacion-remota-de-sectores-y-cronogramas-con-supabase)
5. [Módulo 4: Recibo y Digitalización (OCR y Facturación EPS Tacna)](#modulo-4-recibo-y-digitalizacion-ocr-y-facturacion-eps-tacna)
   - [4.1 Captura Fotográfica y Procesamiento OCR de Recibo Físico](#41-captura-fotografica-y-procesamiento-ocr-de-recibo-fisico)
   - [4.2 Revisión Asistida y Corrección de Campos del Borrador](#42-revision-asistida-y-correccion-de-campos-del-borrador)
   - [4.3 Confirmación, Validación Estricta y Guardado del Recibo](#43-confirmacion-validacion-estricta-y-guardado-del-recibo)
   - [4.4 Registro Manual de Lectura de Medidor Cúbico](#44-registro-manual-de-lectura-de-medidor-cubico)
   - [4.5 Consulta Histórica de Consumo y Detección de Consumo Atípico](#45-consulta-historica-de-consumo-y-deteccion-de-consumo-atipico)
   - [4.6 Sincronización Bidireccional de Recibos con Supabase](#46-sincronizacion-bidireccional-de-recibos-con-supabase)
6. [Módulo 5: Asistente Hídrico Inteligente (n8n & IA)](#modulo-5-asistente-hidrico-inteligente-n8n--ia)
   - [5.1 Envío de Pregunta Ciudadana y Consulta a Webhook n8n](#51-envio-de-pregunta-ciudadana-y-consulta-a-webhook-n8n)
   - [5.2 Observación Reactiva de Conversación y Estados de Escribiendo](#52-observacion-reactiva-de-conversacion-y-estados-de-escribiendo)
   - [5.3 Limpieza y Reinicio de la Conversación](#53-limpieza-y-reinicio-de-la-conversacion)
7. [Módulo 6: Retos y Reportes Ciudadanos (Gamificación y Comunidad)](#modulo-6-retos-y-reportes-ciudadanos-gamificacion-y-comunidad)
   - [7.1 Consulta de Retos Semanales y Posición Relativa en el Sector](#71-consulta-de-retos-semanales-y-posicion-relativa-en-el-sector)
   - [7.2 Marcado de Reto Cumplido y Recálculo de Racha](#72-marcado-de-reto-cumplido-y-recalculo-de-racha)
   - [7.3 Generación y Registro de Reporte Ciudadano con Evidencia Fotográfica](#73-generacion-y-registro-de-reporte-ciudadano-con-evidencia-fotografica)
   - [7.4 Exploración de Incidencias en el Mapa Comunitario](#74-exploracion-de-incidencias-en-el-mapa-comunitario)

---

## Convenciones de Arquitectura y Actores

Los diagramas emplean las siguientes convenciones de participantes:
- **`Usuario`**: Persona interactuando con la interfaz táctil.
- **`UI (Screen / Composable)`**: Pantalla o componente en Jetpack / Compose Multiplatform.
- **`ViewModel`**: Gestor de estado de presentación (`StateFlow`), escucha eventos (`Intent`) y emite `UiState`.
- **`UseCase`**: Clase de lógica de negocio pura en `domain/usecase/`.
- **`Repository`**: Contrato de datos en `domain/repository/` e implementación en `data/`.
- **`DAO / Store`**: Objeto de acceso a datos Room SQLite local (`data/local/`) o almacén en memoria.
- **`Remote / Cloud`**: APIs externas, clientes HTTP Ktor (`Supabase`, `n8n webhook`, Google Auth).
- **`Platform / Hardware`**: Sensores de la plataforma (Cámara, GPS, Sistema de Archivos, WorkManager).

---

## Módulo 1: Sesión, Onboarding y Bienvenida

Custodio transversal del acceso, persistencia del modo de uso (anónimo local vs Google) y comprobación de registro de domicilio inicial.

### 1.1 Verificación de Estado de Sesión y Onboarding (`PuertaDeAcceso`)

Determina la pantalla inicial al abrir la app: si ya inició sesión y configuró su domicilio, va directo al `NavHost` principal; en caso contrario, muestra la bienvenida o el registro de domicilio.

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant App as PuertaDeAcceso (Composable)
    participant VM as AccesoViewModel
    participant Reg as RegistroDeAccesoEnRoom
    participant DAO as UsuarioDao
    participant Nav as AppNavegacion (NavHost)

    Usuario->>App: Abre la aplicación
    App->>VM: Observa uiState (StateFlow)
    activate VM
    VM->>Reg: observar()
    Reg->>DAO: obtenerModoAcceso(usuarioId)
    DAO-->>Reg: ModoDeAcceso (SIN_CUENTA | GOOGLE | null)
    Reg-->>VM: Flow<ModoDeAcceso?>
    VM->>Reg: tieneDomicilio()
    Reg->>DAO: obtenerSector(usuarioId)
    DAO-->>Reg: sectorId (String?)
    Reg-->>VM: Flow<Boolean>
    VM-->>App: AccesoUiState(cargando=false, modo, tieneDomicilio)
    deactivate VM

    alt Sin modo de acceso
        App->>Usuario: Muestra BienvenidaScreen
    else Modo configurado pero sin domicilio
        App->>Usuario: Navega a RegistrarDomicilioScreen
    else Modo y domicilio listos
        App->>Nav: Carga AppNavegacion (Pestaña Reserva / Sector)
        Nav->>Usuario: Renderiza pantalla principal
    end
```

---

### 1.2 Inicio de Sesión Anónimo (`Empezar sin cuenta`)

Permite al ciudadano usar la aplicación de inmediato bajo privacidad total (almacenamiento local en SQLite).

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant Screen as BienvenidaScreen
    participant VM as AccesoViewModel
    participant Reg as RegistroDeAccesoEnRoom
    participant DAO as UsuarioDao
    participant DB as SQLite (Room)

    Usuario->>Screen: Presiona "Empezar sin cuenta"
    Screen->>VM: empezarSinCuenta()
    activate VM
    Note over VM: Valida que consentimiento sea true y no esté enCurso
    VM->>Reg: guardar(ModoDeAcceso.SIN_CUENTA)
    activate Reg
    Reg->>DAO: guardarModoAcceso(usuarioId, "SIN_CUENTA")
    DAO->>DB: INSERT OR REPLACE INTO usuario (id, modoAcceso)
    DB-->>DAO: OK
    DAO-->>Reg: Retorno exitoso
    deactivate Reg
    Reg-->>VM: Emisión reactiva de nuevo ModoDeAcceso
    VM-->>Screen: AccesoUiState(modo = SIN_CUENTA)
    deactivate VM
    Screen->>Usuario: Navega a RegistrarDomicilioScreen (Onboarding inicial)
```

---

### 1.3 Inicio de Sesión con Google (`InicioConGoogle`)

Flujo federado de autenticación con credenciales Google para respaldar datos en la nube.

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant Screen as BienvenidaScreen
    participant VM as AccesoViewModel
    participant Google as InicioConGoogle (expect/actual)
    participant Reg as RegistroDeAccesoEnRoom
    participant DAO as UsuarioDao

    Usuario->>Screen: Presiona "Continuar con Google"
    Screen->>VM: entrarConGoogle()
    activate VM
    VM-->>Screen: AccesoUiState(enCurso = true)
    VM->>Google: iniciar()
    activate Google
    Google->>Usuario: Despliega Selector de Cuentas Google nativo
    Usuario->>Google: Selecciona cuenta y autoriza
    Google-->>VM: ResultadoInicio.Exito(idToken, correo, nombre)
    deactivate Google

    alt Autenticación Exitosa
        VM->>Reg: guardar(ModoDeAcceso.GOOGLE, correo, nombre)
        Reg->>DAO: actualizarSesion(usuarioId, "GOOGLE", correo, nombre)
        DAO-->>Reg: OK
        VM-->>Screen: AccesoUiState(enCurso = false, modo = GOOGLE)
        Screen->>Usuario: Redirige a verificación de domicilio
    else Usuario Cancela o Falla de Red
        Google-->>VM: ResultadoInicio.Fallo(mensajeError)
        VM-->>Screen: AccesoUiState(enCurso = false, mensaje = mensajeError)
        Screen->>Usuario: Muestra Snackbar con mensaje de error
    end
    deactivate VM
```

---

## Módulo 2: Reserva (Gestión Hídrica del Hogar)

Responsable: **Cristhian**. Modela el tanque/cisterna del hogar, calcula la tasa de agotamiento ($L/h$), proyecta la fecha/hora sin agua y emite alertas preventivas.

### 2.1 Configuración Inicial del Hogar (`ConfiguracionViewModel`)

Registro de las características físicas de almacenamiento y ocupantes de la vivienda.

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant UI as ConfiguracionScreen
    participant VM as ConfiguracionViewModel
    participant UC as ConfigurarHogar (UseCase)
    participant Repo as ReservaRepositoryImpl
    participant DAO as ReservaDao
    participant DB as SQLite (Room)

    Usuario->>UI: Ingresa capacidad (litros), tipo (Tanque/Cisterna), número de habitantes y hábitos
    Usuario->>UI: Presiona "Guardar configuración"
    UI->>VM: alEvento(Guardar)
    activate VM
    VM->>UC: invoke(tipoReservorio, capacidad, habitantes, habitos)
    activate UC
    UC->>UC: Validar límites (capacidad > 0, habitantes >= 1)
    UC->>Repo: guardarPerfil(configuracionHogar, consumoPorHabitos)
    deactivate UC
    activate Repo
    Repo->>Repo: Crear PerfilHogar con usuarioId
    Repo->>DAO: guardarPerfil(PerfilHogarEntity)
    DAO->>DB: INSERT OR REPLACE INTO perfil_hogar (...)
    DB-->>DAO: OK
    DAO-->>Repo: Confirmación
    Repo-->>VM: Result.success(Unit)
    deactivate Repo
    VM-->>UI: ConfiguracionUiState(guardado = true)
    deactivate VM
    UI->>Usuario: Navega hacia la pantalla principal de Reserva
```

---

### 2.2 Registro de Evento de Llenado (Real vs Confirmación de Asumido)

Cuando la red pública abastece agua, el usuario registra el llenado o confirma el llenado automático estimado por el cronograma del sector.

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant UI as ReservaScreen
    participant VM as ReservaViewModel
    participant Repo as ReservaRepositoryImpl
    participant DAO as ReservaDao
    participant DB as SQLite (Room)

    alt Caso A: Registro Manual Inmediato
        Usuario->>UI: Toca botón "Registrar Llenado" (Completo / Parcial)
        UI->>VM: alEvento(RegistrarLlenado(tipo))
        activate VM
        VM->>Repo: registrarLlenado(ahora, tipo)
        activate Repo
        Repo->>Repo: require(momento <= ahora)
        Repo->>DAO: guardarLlenado(EventoLlenadoEntity(id, usuarioId, momento, tipo))
        DAO->>DB: INSERT INTO evento_llenado VALUES (...)
        Repo->>DAO: guardarPerfil(perfil con consumoVigente = null)
        Note over Repo,DAO: Se resetea el consumo fijado para recalcular dinámicamente
        DAO-->>Repo: OK
        Repo-->>VM: Result.success(Unit)
        deactivate Repo
    else Caso B: Confirmación de Llenado Asumido (Cronograma)
        Note over UI: La app detectó que pasó la ventana de abastecimiento
        Usuario->>UI: Presiona "Sí, se llenó" (Confirmar asumido)
        UI->>VM: alEvento(ConfirmarLlenadoAsumido)
        VM->>Repo: registrarLlenado(llenadoAsumido.momento, TipoLlenado.COMPLETO)
        activate Repo
        Repo->>DAO: guardarLlenado(EventoLlenadoEntity)
        DAO->>DB: INSERT INTO evento_llenado VALUES (...)
        DAO-->>Repo: OK
        Repo-->>VM: Result.success(Unit)
        deactivate Repo
    end
    deactivate VM
    Note over DAO,VM: Room emite actualización reactiva vía Flow<EventoLlenado>
    VM-->>UI: UI se actualiza con nivel al 100%
```

---

### 2.3 Monitoreo Reactivo y Proyección Continua de Agotamiento

Flujo principal de la pantalla de Reserva: orquesta el tiempo transcurrido, resta el consumo estimado por habitante/hora y calcula el déficit frente a la próxima llegada de agua.

```mermaid
sequenceDiagram
    autonumber
    participant Reloj as Reloj (Tick cada minuto)
    participant UI as ReservaScreen
    participant VM as ReservaViewModel
    participant Repo as ReservaRepositoryImpl
    participant Sector as AbastecimientosDeSector
    participant Vista as ConstruirVistaReserva
    participant Estimar as EstimarConsumo

    Note over VM: Init() combina: observarPerfil(), observarReserva(), observarAvisos(), reloj
    Reloj->>VM: Tick minutal (Flow emit)
    activate VM
    VM->>Repo: observarReserva()
    Repo->>Estimar: estimar(historialIntervalos, capacidad)
    Estimar-->>Repo: ConsumoHorario (L/h)
    Repo-->>VM: Reserva(nivelActual, consumo, agotamientoProyectado)
    VM->>Sector: proximoDesde(momentoActual)
    Sector-->>VM: ProximoAbastecimiento(fechaHora, horasRestantes)
    VM->>Repo: litrosPorHabitanteDia()
    Repo-->>VM: LitrosPorHabitanteDia (L/hab/día)
    VM->>Vista: invoke(reserva, contextoHogar, proximoAbastecimiento, lhd, ahora)
    activate Vista
    Note over Vista: Calcula porcentaje (0-100%), horas de reserva,<br/>déficit de agua si se agota antes del turno
    Vista-->>VM: VistaReserva(nivelLitros, porcentaje, estado, avisoDeficit)
    deactivate Vista
    VM-->>UI: ReservaUiState(cargando=false, vista=VistaReserva)
    deactivate VM
    UI->>Usuario: Renderiza tanque interactivo, estado de reserva y tarjeta de alerta
```

---

### 2.4 Declaración de Agotamiento Real (`Me quedé sin agua`) y Recalibración

Cuando el agua se acaba antes de lo proyectado, el usuario lo declara. El sistema recalibra la tasa de consumo horaria con un límite de cambio prudente (*anti-error de dedo*).

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant UI as SinAguaScreen
    participant VM as SinAguaViewModel
    participant Repo as ReservaRepositoryImpl
    participant UC as DeclararSinAgua (UseCase)
    participant DAO as ReservaDao
    participant DB as SQLite (Room)

    Usuario->>UI: Accede y confirma "¿Te quedaste sin agua?"
    UI->>VM: declararSinAgua()
    activate VM
    VM->>Repo: declararSinAgua(momentoActual)
    activate Repo
    Repo->>Repo: simularSinAgua(momentoActual)
    Repo->>UC: invoke(reservaActual, intervalosHistorial, momentoActual)
    activate UC
    Note over UC: Si el último llenado fue REAL, genera un<br/>IntervaloConsumo(OBSERVADO) exacto
    UC->>UC: Recalcula consumo con tope (+/- 30% máx)
    UC-->>Repo: ResultadoSinAgua(nuevaReserva, intervaloObservado)
    deactivate UC
    Repo->>DAO: guardarNovedad(NovedadReservaEntity(tipo = SIN_AGUA))
    DAO->>DB: INSERT INTO novedad_reserva VALUES (...)
    Repo->>DAO: guardarPerfil(perfil con nuevo consumoVigente)
    DAO->>DB: UPDATE perfil_hogar SET consumoVigente = nuevoConsumo
    DB-->>DAO: OK
    DAO-->>Repo: OK
    Repo-->>VM: Result.success(Unit)
    deactivate Repo
    VM-->>UI: SinAguaUiState(declarado = true)
    deactivate VM
    UI->>Usuario: Notifica recalibración exitosa y regresa a Reserva
```

---

### 2.5 Simulación y Sugerencia de Recortes de Consumo (`¿Qué recortar?`)

Algoritmo heurístico que aconseja qué actividades reducir (duchas, lavado de ropa, riego) cuando la reserva no alcanzará hasta el próximo turno de agua.

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant UI as QueRecortarScreen
    participant VM as QueRecortarViewModel
    participant Sugerir as SugerirRecortes (UseCase)
    participant Simular as SimularRecortes (UseCase)
    participant Repo as ReservaRepositoryImpl

    Usuario->>UI: Abre pantalla "¿Qué recortar para llegar?"
    UI->>VM: Carga inicial / Observar estado
    activate VM
    VM->>Repo: Cargar Reserva y Estado actual
    Repo-->>VM: Reserva (déficit existente)
    VM->>Sugerir: invoke(reserva, proximoTurno)
    activate Sugerir
    Note over Sugerir: Evalúa actividades prescindibles según hábitos<br/>y litros ahorrables por recorte
    Sugerir-->>VM: List<RecomendacionRecorte>
    deactivate Sugerir
    VM-->>UI: QueRecortarUiState(recomendaciones, recortesSeleccionados)
    deactivate VM

    Usuario->>UI: Marca / desmarca un recorte sugerido (ej. "No lavar ropa hoy")
    UI->>VM: alternarRecorte(idRecorte)
    activate VM
    VM->>Simular: invoke(reserva, recortesActivos)
    Simular-->>VM: SimulacionRecortes(nuevoDeficit, horasGanadas, alcanzaLlegar)
    VM-->>UI: QueRecortarUiState(simulacionActualizada)
    deactivate VM
    UI->>Usuario: Muestra en tiempo real las horas adicionales que ganaría la reserva
```

---

### 2.6 Tarea Periódica de Recálculo y Emisión de Avisos Preventivos (Worker)

Ejecución en segundo plano horaria (vía WorkManager en Android) para alertar al usuario antes de que se quede sin agua, sin necesidad de abrir la app.

```mermaid
sequenceDiagram
    autonumber
    participant WM as WorkManager (Background Worker)
    participant UC as RecalcularYAvisar (UseCase)
    participant Eval as EvaluarAvisos
    participant Repo as ReservaRepositoryImpl
    participant Sector as AbastecimientosDeSector
    participant Reg as RegistroDeAvisosEnRoom
    participant Notif as Notificador (Platform Notification)
    actor Usuario

    WM->>UC: invoke(ahora = LocalDateTime)
    activate UC
    UC->>Repo: observarReserva().first()
    Repo-->>UC: ReservaActual
    UC->>Sector: proximoDesde(ahora)
    Sector-->>UC: ProximoAbastecimiento
    UC->>Eval: invoke(reserva, proximo, ahora)
    activate Eval
    Note over Eval: Evalúa umbrales:<br/>- ALERTA_CRITICA (< 6 horas)<br/>- DEFICIT_CONFIRMADO<br/>- LLENADO_ASUMIDO
    Eval-->>UC: Aviso? (ej. Aviso.AguaSeAgotaAntesDelTurno)
    deactivate Eval

    alt Hay un aviso que dar
        UC->>Reg: yaSeAviso(aviso.clave)
        Reg-->>UC: false (no se ha emitido aún)
        UC->>Reg: registrar(aviso, ahora)
        Reg->>Reg: Guarda en tabla aviso_reserva (Room)
        UC->>Notif: mostrar(aviso)
        activate Notif
        Notif->>Usuario: Muestra Notificación Push Local en la barra del SO
        deactivate Notif
    else No corresponde aviso o ya fue avisado
        UC-->>WM: Retorna null (omite notificación repetida)
    end
    deactivate UC
```

---

### 2.7 Sincronización en la Nube con Supabase (`SincronizadorReserva`)

Garantiza persistencia y respaldo en el backend cuando se detecta conexión a internet.

```mermaid
sequenceDiagram
    autonumber
    participant Sync as SincronizadorReserva
    participant DAO as ReservaDao
    participant Cloud as NubeReservaSupabase
    participant Supa as Supabase Postgres / REST

    Sync->>DAO: obtenerPerfil(usuarioId)
    DAO-->>Sync: PerfilHogarEntity
    Sync->>DAO: obtenerLlenadosNoSincronizados()
    DAO-->>Sync: List<EventoLlenadoEntity>
    activate Cloud
    Sync->>Cloud: subirPerfil(perfil)
    Cloud->>Supa: POST /rest/v1/perfil_hogar (upsert)
    Supa-->>Cloud: 200 OK
    Sync->>Cloud: subirLlenados(llenados)
    Cloud->>Supa: POST /rest/v1/evento_llenado (upsert)
    Supa-->>Cloud: 201 Created
    deactivate Cloud
    Sync->>DAO: marcarComoSincronizados(idsLlenados)
    DAO-->>Sync: OK
```

---

## Módulo 3: Sector y Abastecimiento (Horarios y Cisternas)

Responsable: **Dayan**. Administra los 14+ sectores operacionales de Tacna, cronogramas de tandeo, confirmaciones ciudadanas de horarios y red de cisternas.

### 3.1 Detección Espacial y Registro de Domicilio / Sector

El usuario ubica su domicilio vía GPS o pin en el mapa interactivo; el dominio calcula la pertenencia geográfica al sector.

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant UI as RegistrarDomicilioScreen
    participant VM as RegistrarDomicilioViewModel
    participant UC as ResolverSector (UseCase)
    participant Repo as SectorRepositoryImpl
    participant DAO as SectorDao
    participant UserDAO as UsuarioDao

    Usuario->>UI: Toca "Usar mi ubicación GPS" o selecciona punto en mapa
    UI->>VM: marcarEnMapa(coordenada)
    activate VM
    VM->>Repo: obtenerSectores()
    Repo-->>VM: List<Sector> (con polígonos y radios)
    VM->>UC: resolver(coordenada, sectores)
    activate UC
    Note over UC: Algoritmo Point-in-Polygon / Haversine<br/>Determina el sector exacto
    UC-->>VM: Sector (ej. "Sector 07 - Cono Sur")
    deactivate UC
    VM->>Repo: obtenerCronogramas(sector.id)
    Repo-->>VM: List<Cronograma>
    VM-->>UI: RegistrarDomicilioUiState(sector, continuidad="4h/día", etiqueta="SECTOR 07")
    deactivate VM

    Usuario->>UI: Presiona "Confirmar Domicilio"
    UI->>VM: confirmarSector()
    activate VM
    VM->>Repo: guardarUbicacionCasa(coordenada)
    Repo->>DAO: guardarDomicilio(DomicilioEntity(usuarioId, lat, lon))
    VM->>UserDAO: guardarSectorEnUsuario(sector.id)
    UserDAO-->>VM: OK
    VM-->>UI: RegistrarDomicilioUiState(guardado = true)
    deactivate VM
    UI->>Usuario: Finaliza configuración y transiciona a vista general
```

---

### 3.2 Consulta de Cronograma Vigente y Próximo Abastecimiento

Cálculo dinámico del estado del servicio de agua (¿hay agua en este momento? y ¿cuántas horas faltan para la próxima apertura?).

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant UI as SectorScreen
    participant VM as SectorViewModel
    participant Repo as SectorRepositoryImpl
    participant UC_Vigente as ObtenerCronogramaVigente
    participant UC_Proximo as ProximoAbastecimiento
    participant Cisternas as BuscarCisternasCercanas

    Usuario->>UI: Abre pestaña Sector
    UI->>VM: Carga inicial (cargarSector)
    activate VM
    VM->>Repo: obtenerUbicacionCasa()
    Repo-->>VM: Coordenada (Casa)
    VM->>Repo: obtenerSectores()
    Repo-->>VM: List<Sector>
    VM->>Repo: obtenerCronogramas(sector.id)
    Repo-->>VM: List<Cronograma> (Horas de apertura y corte)
    VM->>UC_Vigente: obtener(cronogramas, momentoActual)
    activate UC_Vigente
    Note over UC_Vigente: Comprueba si momentoActual cae<br/>dentro de [horaInicio, horaFin]
    UC_Vigente-->>VM: CronogramaActivo? (hayAguaAhora = Boolean)
    deactivate UC_Vigente

    VM->>UC_Proximo: calcular(cronogramas, momentoActual)
    activate UC_Proximo
    UC_Proximo-->>VM: ProximoAbastecimiento(fecha, horaInicio, horasFaltantes)
    deactivate UC_Proximo

    VM->>Repo: obtenerPuntosCisterna(sector.id)
    Repo-->>VM: List<PuntoCisterna>
    VM->>Cisternas: buscar(puntos, casa, radioKm = 2.0)
    Cisternas-->>VM: List<CisternaCercana>

    VM->>Repo: obtenerConfirmaciones(sector.id, fechaHoy)
    Repo-->>VM: List<ConfirmacionHorario>

    VM-->>UI: SectorUiState(aguaLlegandoAhora, proximo, cisternas, confirmacionesCount)
    deactivate VM
    UI->>Usuario: Muestra tarjeta principal ("Llegando ahora" o "Próximo tandeo a las 05:00")
```

---

### 3.3 Confirmación Colaborativa Comunitaria (Llegada / Corte de Agua)

Los vecinos notifican en tiempo real la llegada o el corte físico del agua en su calle/sector.

```mermaid
sequenceDiagram
    autonumber
    actor Vecino as Usuario (Vecino)
    participant UI as TarjetasSector (Composable)
    participant VM as SectorViewModel
    participant Repo as SectorRepositoryImpl
    participant DAO as SectorDao
    participant Nube as NubeSectorSupabase
    participant Supa as Supabase (Cloud)

    Vecino->>UI: Toca botón "¡Llegó el agua!" o "Se cortó el agua"
    UI->>VM: confirmar(TipoConfirmacion.LLEGADA)
    activate VM
    VM->>Repo: registrarConfirmacion(ConfirmacionHorario(id, sectorId, usuarioId, momento, LLEGADA))
    activate Repo
    Repo->>DAO: guardarConfirmacion(ConfirmacionHorarioEntity)
    DAO->>DAO: INSERT INTO confirmacion_horario VALUES (...)
    Repo->>Nube: enviarConfirmacion(confirmacion)
    activate Nube
    Nube->>Supa: POST /rest/v1/confirmacion_horario
    Supa-->>Nube: 201 Created
    deactivate Nube
    Repo-->>VM: OK
    deactivate Repo
    VM->>Repo: obtenerConfirmaciones(sector.id, fechaHoy)
    Repo-->>VM: Lista actualizada con la nueva confirmación
    VM-->>UI: SectorUiState(confirmacionesDeHoy = count + 1, mensajeConfirmado)
    deactivate VM
    UI->>Vecino: Muestra feedback táctil y chip "Confirmado por ti y N vecinos hoy"
```

---

### 3.4 Consolidación Algorítmica de Cronograma Colaborativo por Mediana

Consolida los reportes comunitarios y filtra anomalías estadísticas mediante la mediana para ajustar la hora de corte real.

```mermaid
sequenceDiagram
    autonumber
    participant Cron as Tarea de Consolidación
    participant UC as ConsolidarCronogramaColaborativo
    participant Repo as SectorRepositoryImpl
    participant DAO as SectorDao

    Cron->>Repo: obtenerConfirmaciones(sectorId, fecha)
    Repo-->>Cron: List<ConfirmacionHorario>
    Cron->>UC: consolidar(sectorId, fecha, confirmaciones)
    activate UC
    Note over UC: Filtra llegadas y cortes del día.<br/>Requiere mínimo N confirmaciones válidas.
    alt Confirmaciones insuficientes (< mínimo)
        UC-->>Cron: null (Se mantiene horario oficial)
    else Muestra estadística suficiente
        UC->>UC: Calcular mediana(segundosLlegada)
        UC->>UC: Calcular mediana(segundosCorte)
        Note over UC: La mediana evita que un reporte errado<br/>a las 3pm desplace el promedio de las 6am
        UC-->>Cron: Cronograma(tipo = PROGRAMADO, fuente = COLABORATIVA, horaInicio, horaFin)
    end
    deactivate UC
    alt Cronograma consolidado generado
        Cron->>Repo: guardarCronograma(cronogramaColaborativo)
        Repo->>DAO: guardarCronograma(CronogramaEntity)
    end
```

---

### 3.5 Búsqueda y Localización Espacial de Puntos de Cisterna

Muestra los puntos habilitados de reparto alternativo de agua mediante camiones cisterna de la EPS.

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant UI as PuntosCisternaScreen
    participant VM as PuntosCisternaViewModel
    participant Repo as SectorRepositoryImpl
    participant UC as BuscarCisternasCercanas
    participant Mapa as MapaCisternas (Compose)

    Usuario->>UI: Accede a "Puntos de Cisterna"
    UI->>VM: cargarPuntos()
    activate VM
    VM->>Repo: obtenerUbicacionCasa()
    Repo-->>VM: CoordenadaCasa
    VM->>Repo: obtenerPuntosCisterna(sectorId)
    Repo-->>VM: List<PuntoCisterna> (Coordenadas, referencia, horario)
    VM->>UC: buscar(puntos, casa, radioKm = 3.0)
    activate UC
    Note over UC: Ordena por distancia euclidiana / haversine<br/>Filtra puntos dentro del rango operativo
    UC-->>VM: List<CisternaCercana(punto, distanciaMetros)>
    deactivate UC
    VM-->>UI: PuntosCisternaUiState(cargando=false, cisternas)
    deactivate VM
    UI->>Mapa: Dibuja marcadores de cisterna y ruta estimada
    Mapa->>Usuario: Renderiza mapa con pines y distancia en metros/km
```

---

### 3.6 Sincronización Remota de Sectores y Cronogramas con Supabase

Descarga de las fuentes oficiales de EPS Tacna almacenadas en la base centralizada.

```mermaid
sequenceDiagram
    autonumber
    participant Sync as SincronizadorSector
    participant Nube as NubeSectorSupabase
    participant Supa as Supabase REST API
    participant DAO as SectorDao

    Sync->>Nube: descargarSectores()
    activate Nube
    Nube->>Supa: GET /rest/v1/sector?select=*
    Supa-->>Nube: 200 OK (JSON Sectores)
    deactivate Nube
    Nube-->>Sync: List<SectorEntity>
    Sync->>DAO: guardarSectores(sectores)

    Sync->>Nube: descargarCronogramasVigentes()
    activate Nube
    Nube->>Supa: GET /rest/v1/cronograma?fecha=gte.hoy
    Supa-->>Nube: 200 OK (JSON Cronogramas)
    deactivate Nube
    Nube-->>Sync: List<CronogramaEntity>
    Sync->>DAO: guardarCronogramas(cronogramas)
    DAO-->>Sync: Base local actualizada
```

---

## Módulo 4: Recibo y Digitalización (OCR y Facturación EPS Tacna)

Responsable: **Iker**. Extrae datos de la boleta de agua física mediante OCR en el dispositivo, valida coherencia volumétrica y registra el historial de facturación.

### 4.1 Captura Fotográfica y Procesamiento OCR de Recibo Físico

Flujo desde que el usuario enfoca la boleta hasta la extracción estructurada de campos (período, consumo $m^3$, importe S/, lecturas).

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant Cam as CamaraReciboScreen
    participant VM as CapturaViewModel
    participant CamaraUtil as capturaFoto (expect/actual)
    participant UC as EscanearReciboUseCase
    participant OCR as ReconocedorTextoPlataforma (MLKit)
    participant Parser as ParserReciboEpsTacna
    participant Store as BorradorReciboStore

    Usuario->>Cam: Presiona botón "Capturar Recibo"
    Cam->>CamaraUtil: dispararCaptura()
    CamaraUtil-->>Cam: bytesImagen (ByteArray)
    Cam->>VM: onFotoCapturada(bytesImagen)
    activate VM
    VM-->>Cam: CapturaUiState.Procesando (Spinner)
    VM->>UC: invoke(bytesImagen)
    activate UC
    UC->>OCR: reconocer(bytesImagen)
    activate OCR
    Note over OCR: Procesa texto por bloques y líneas en el dispositivo
    OCR-->>UC: TextoReconocido (bloques, líneas, cadenas)
    deactivate OCR

    UC->>Parser: parsear(textoReconocido)
    activate Parser
    Note over Parser: ReconstructorFilas: busca palabras clave:<br/>"EPS TACNA", "MES FACTURADO",<br/>"LECTURA ACTUAL/ANTERIOR", "TOTAL S/"
    Parser-->>UC: ResultadoParseo.Exito(ReciboBorrador)
    deactivate Parser

    UC-->>VM: Result.success(ReciboBorrador)
    deactivate UC

    VM->>Store: guardar(ReciboBorrador)
    Note over VM: Libera bytes de la foto en memoria RAM
    VM-->>Cam: CapturaUiState.Exito(borrador)
    deactivate VM
    Cam->>Usuario: Transiciona automáticamente a RevisionScreen
```

---

### 4.2 Revisión Asistida y Corrección de Campos del Borrador

Si un número fue interpretado con baja confianza (o borroso), el usuario lo edita antes de guardarlo.

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant UI as ConfirmarCamposScreen / RevisionScreen
    participant VM as RevisionViewModel
    participant VM_Corr as CorreccionViewModel
    participant UC_Corr as CorregirCampoUseCase
    participant Store as BorradorReciboStore

    Usuario->>UI: Observa campos (Lectura Anterior, Actual, Consumo m3, Total S/)
    Note over UI: Si un campo tiene alerta visual, el usuario lo toca para corregir
    Usuario->>UI: Toca "Consumo m³" e ingresa "22"
    UI->>VM_Corr: alCambiarValor(campo = CONSUMO_M3, nuevoValor = "22")
    activate VM_Corr
    VM_Corr->>UC_Corr: invoke(borradorActual, TipoCampo.CONSUMO_M3, "22")
    activate UC_Corr
    UC_Corr->>UC_Corr: Recalcula consistencia (ej: Actual - Anterior == Consumo)
    UC_Corr-->>VM_Corr: BorradorModificado
    deactivate UC_Corr
    VM_Corr->>Store: actualizar(BorradorModificado)
    Store-->>VM: Emisión reactiva del borrador actualizado
    VM-->>UI: RevisionUiState(borrador = BorradorModificado, esValido = true)
    deactivate VM_Corr
    UI->>Usuario: Muestra campo con check verde de validación
```

---

### 4.3 Confirmación, Validación Estricta y Guardado del Recibo

Persistencia en base de datos Room verificando que no existan duplicados para el mismo mes facturado.

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant UI as RevisionScreen
    participant VM as RevisionViewModel
    participant UC as ConfirmarReciboUseCase
    participant Val as ValidadorRecibo
    participant Repo as ReciboRepositoryRoom
    participant DAO as ReciboDao
    participant DB as SQLite (Room)

    Usuario->>UI: Presiona botón "Confirmar y Guardar Recibo"
    UI->>VM: confirmarRecibo()
    activate VM
    VM->>UC: invoke(borradorActual)
    activate UC
    UC->>Val: validar(borrador)
    Val-->>UC: Validacion(ok = true)
    UC->>Repo: obtenerPorPeriodo(borrador.periodoConsumo)
    activate Repo
    Repo->>DAO: buscarPorPeriodo(periodo)
    DAO-->>Repo: ReciboEntity?
    deactivate Repo

    alt Recibo existente con ID diferente (Duplicado)
        UC-->>VM: ResultadoConfirmacion.Duplicado(periodo)
        VM-->>UI: Muestra diálogo "¿Deseas reemplazar el recibo de este mes?"
    else Recibo Nuevo o Reemplazo Autorizado
        UC->>UC: Asigna nuevoId() "recibo-uuid"
        UC->>Repo: guardar(Recibo)
        activate Repo
        Repo->>DAO: insertarOActualizar(ReciboEntity)
        DAO->>DB: INSERT OR REPLACE INTO recibo VALUES (...)
        DB-->>DAO: OK
        DAO-->>Repo: OK
        deactivate Repo
        UC-->>VM: ResultadoConfirmacion.Guardado(recibo, reemplazo = false)
        VM-->>UI: RevisionUiState(guardadoExitoso = true)
        UI->>Usuario: Muestra confirmación y redirige a ReciboHistorialScreen
    end
    deactivate UC
    deactivate VM
```

---

### 4.4 Registro Manual de Lectura de Medidor Cúbico

Alternativa a la foto: ingreso de los dígitos del dial del medidor hogareño para estimar el consumo intermedio.

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant UI as ReciboManualMedidorScreen
    participant Teclado as TecladoNumericoMedidor
    participant VM as CapturaViewModel
    participant Store as BorradorReciboStore
    participant UC as ConfirmarReciboUseCase

    Usuario->>UI: Selecciona "Ingresar datos a mano"
    UI->>VM: iniciarManual()
    VM->>Store: guardar(ReciboBorrador.vacio(periodoActual))
    UI->>Usuario: Muestra display de dígitos de medidor (negros/rojos)
    Usuario->>Teclado: Digita "00452" (metros cúbicos actuales)
    Teclado->>UI: Actualiza dígitos en pantalla
    Usuario->>UI: Presiona "Continuar"
    UI->>Store: actualizarLectura(452.0)
    UI->>Usuario: Transiciona a revisión para completar el período
```

---

### 4.5 Consulta Histórica de Consumo y Detección de Consumo Atípico

Gráficos de barras de evolución mensual ($m^3$) y diagnóstico de posibles fugas no visibles.

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant UI as ReciboHistorialScreen
    participant VM as HistorialViewModel
    participant UC_Hist as ObservarHistorialUseCase
    participant UC_Resumen as ObservarResumenUseCase
    participant Eval as EvaluadorConsumo
    participant Repo as ReciboRepositoryRoom
    participant DAO as ReciboDao

    Usuario->>UI: Ingresa a "Historial de Recibos"
    UI->>VM: Observa estado del historial
    activate VM
    VM->>UC_Hist: invoke()
    activate UC_Hist
    UC_Hist->>Repo: observarRecibos()
    Repo->>DAO: obtenerTodosOrdenadosPorPeriodo()
    DAO-->>Repo: Flow<List<ReciboEntity>>
    Repo-->>UC_Hist: Flow<List<Recibo>>
    deactivate UC_Hist

    VM->>UC_Resumen: invoke()
    activate UC_Resumen
    UC_Resumen->>Eval: calcularPromedioHistorico(recibos)
    Eval-->>UC_Resumen: PromedioM3 (ej. 14.5 m3)
    UC_Resumen->>Eval: detectarConsumoAtipico(ultimoRecibo, promedio)
    activate Eval
    Note over Eval: Si ultimo.m3 > promedio * 1.5<br/>Marca bandera de consumo atípico / posible fuga
    Eval-->>UC_Resumen: ConsumoAtipico(esAtipico=true, porcentajeExceso=+60%)
    deactivate Eval
    UC_Resumen-->>VM: ResumenConsumo(promedio, atipico, tendencia)
    deactivate UC_Resumen

    VM-->>UI: HistorialUiState(recibos, resumen, alertaFugaVisible = true)
    deactivate VM
    UI->>Usuario: Dibuja gráfico de barras y banner de advertencia de fuga
```

---

### 4.6 Sincronización Bidireccional de Recibos con Supabase

Respaldo cifrado de las facturas históricas en el repositorio en la nube.

```mermaid
sequenceDiagram
    autonumber
    participant Sync as SincronizadorRecibo
    participant DAO as ReciboDao
    participant Nube as NubeReciboSupabase
    participant Supa as Supabase (PostgreSQL)

    Sync->>DAO: obtenerRecibosPendientesDeSubida()
    DAO-->>Sync: List<ReciboEntity>
    loop Por cada recibo no sincronizado
        Sync->>Nube: subirRecibo(recibo)
        activate Nube
        Nube->>Supa: POST /rest/v1/recibo (Upsert por id)
        Supa-->>Nube: 201 Created / 200 OK
        deactivate Nube
        Sync->>DAO: marcarSincronizado(recibo.id, true)
        DAO-->>Sync: OK
    end
```

---

## Módulo 5: Asistente Hídrico Inteligente (n8n & IA)

Integración conversacional para resolver dudas sobre normativas Sunass, lectura de recibos, reclamos por cortes imprevistos y técnicas de ahorro.

### 5.1 Envío de Pregunta Ciudadana y Consulta a Webhook n8n

Envío de consulta, mantenimiento de sesión conversacional y recepción de respuesta del agente IA.

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant UI as AsistenteScreen
    participant VM as AsistenteViewModel
    participant UC as EnviarMensajeUseCase
    participant Repo as AsistenteRepositoryImpl
    participant Client as N8nApiClient (Ktor)
    participant Webhook as Webhook n8n (Agente IA)

    Usuario->>UI: Escribe "¿Cómo puedo reclamar un cobro excesivo?" y presiona Enviar
    UI->>VM: enviarMensaje()
    activate VM
    VM->>VM: Limpia caja de texto y activa estaEscribiendo = true
    VM->>UC: invoke(textoLimpio)
    activate UC
    UC->>Repo: enviarMensaje(textoLimpio)
    activate Repo
    Repo->>Repo: Agrega mensaje de usuario al Flow local
    Repo-->>VM: Emisión inmediata (Burbuja usuario aparece en pantalla)

    Repo->>Client: enviarPregunta(texto, sessionId, timestamp)
    activate Client
    Client->>Webhook: POST /webhook/asistente-agua (JSON body con mensaje y session)
    activate Webhook
    Note over Webhook: Flujo n8n: Clasificación de intención,<br/>RAG con base de conocimiento EPS Tacna y respuesta
    Webhook-->>Client: 200 OK {"output": "Para reclamar un cobro excesivo debes..."}
    deactivate Webhook
    Client-->>Repo: String respuesta
    deactivate Client

    Repo->>Repo: Crea MensajeAsistente(esUsuario = false, texto = respuesta)
    Repo-->>UC: Result.success(MensajeAsistente)
    deactivate Repo
    UC-->>VM: Result.success
    deactivate UC
    VM->>VM: estaEscribiendo = false
    VM-->>UI: AsistenteUiState(mensajes, estaEscribiendo = false)
    deactivate VM
    UI->>Usuario: Despliega respuesta del asistente con animación de entrada
```

---

### 5.2 Observación Reactiva de Conversación y Estados de Escribiendo

Manejo del indicador de "pensando / escribiendo" y visualización reactiva de las burbujas de diálogo.

```mermaid
sequenceDiagram
    autonumber
    participant UI as AsistenteScreen
    participant VM as AsistenteViewModel
    participant UC_Obs as ObservarMensajesUseCase
    participant Repo as AsistenteRepositoryImpl
    participant Ind as IndicadorEscribiendo (Composable)

    UI->>VM: Recolecta uiState (StateFlow)
    activate VM
    VM->>UC_Obs: invoke()
    UC_Obs->>Repo: observarMensajes()
    Repo-->>VM: Flow<List<MensajeAsistente>>
    VM-->>UI: AsistenteUiState(mensajes, estaEscribiendo)
    deactivate VM

    alt estaEscribiendo == true
        UI->>Ind: Renderiza burbuja con animación de tres puntos suspensivos
    else estaEscribiendo == false
        UI->>Ind: Oculta indicador
    end
```

---

### 5.3 Limpieza y Reinicio de la Conversación

Permite al usuario vaciar el historial en memoria para iniciar una nueva consulta aislada.

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant UI as AsistenteScreen
    participant VM as AsistenteViewModel
    participant UC as LimpiarConversacionUseCase
    participant Repo as AsistenteRepositoryImpl

    Usuario->>UI: Toca icono de menú "Reiniciar conversación"
    UI->>VM: reiniciarConversacion()
    activate VM
    VM->>UC: invoke()
    activate UC
    UC->>Repo: limpiarConversacion()
    activate Repo
    Repo->>Repo: _mensajes.value = emptyList()
    deactivate Repo
    deactivate UC
    VM->>VM: Reset de variables (_textoEntrada, _estaEscribiendo = false)
    VM-->>UI: AsistenteUiState(mensajes = [])
    deactivate VM
    UI->>Usuario: Muestra pantalla de chat vacía con sugerencias de preguntas iniciales
```

---

## Módulo 6: Retos y Reportes Ciudadanos (Gamificación y Comunidad)

Responsable: **Jimmy**. Incentiva la cultura de ahorro hídrico (retos y rachas) y permite alertar fugas en vía pública a la comunidad.

### 6.1 Consulta de Retos Semanales y Posición Relativa en el Sector

Carga de las misiones semanales de ahorro y comparación del consumo personal contra el promedio barrial.

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant UI as RetosScreen
    participant VM as RetosViewModel
    participant UC_Retos as ObtenerRetosSemana
    participant UC_Comp as CompararConSector
    participant UC_Racha as CalcularRacha
    participant Repo as RetosRepository

    Usuario->>UI: Ingresa a pestaña "Comunidad y Retos"
    UI->>VM: Carga inicial (cargar())
    activate VM
    VM->>UC_Retos: ejecutar()
    activate UC_Retos
    UC_Retos->>Repo: obtenerRetosSemana()
    Repo-->>UC_Retos: List<Reto> (ej. "Duchas de 4 minutos", "Reusar agua de lavado")
    deactivate UC_Retos

    VM->>Repo: obtenerCumplimientos()
    Repo-->>VM: List<RetoUsuario>
    VM->>UC_Racha: calcular(cumplimientos, fechaActual)
    UC_Racha-->>VM: Racha (días consecutivos cumpliendo retos)

    VM->>UC_Comp: ejecutar(sectorId, consumoLhd)
    activate UC_Comp
    Note over UC_Comp: Compara consumo del hogar (92 L/hab/día)<br/>contra percentil del sector (ej. Top 15% más eficiente)
    UC_Comp-->>VM: PosicionSector (puesto, medalla)
    deactivate UC_Comp

    VM-->>UI: RetosUiState(retos, cumplidos, racha, posicionSector)
    deactivate VM
    UI->>Usuario: Despliega tarjetas de retos, insignia de racha y comparativa
```

---

### 6.2 Marcado de Reto Cumplido y Recálculo de Racha

El usuario reporta el cumplimiento de una acción de ahorro diario; el sistema actualiza su racha.

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant UI as RetosContenido (Composable)
    participant VM as RetosViewModel
    participant UC_Marcar as MarcarRetoCumplido
    participant UC_Racha as CalcularRacha
    participant Repo as RetosRepository
    participant DAO as RetosDao

    Usuario->>UI: Marca checkbox "Reto cumplido"
    UI->>VM: completar(retoId)
    activate VM
    VM->>UC_Marcar: ejecutar(retoId)
    activate UC_Marcar
    UC_Marcar->>Repo: marcarCumplido(retoId, fechaHoy)
    activate Repo
    Repo->>DAO: guardarRetoCumplido(RetoUsuarioEntity)
    DAO-->>Repo: OK
    deactivate Repo
    deactivate UC_Marcar

    VM->>Repo: obtenerCumplimientos()
    Repo-->>VM: Lista actualizada
    VM->>UC_Racha: calcular(cumplimientosActualizados, fechaHoy)
    UC_Racha-->>VM: Nueva Racha (+1 día)

    VM-->>UI: RetosUiState(cumplidos += retoId, racha, mensaje = "¡Reto cumplido!")
    deactivate VM
    UI->>Usuario: Muestra animación de confeti / medalla y actualiza contador de racha
```

---

### 6.3 Generación y Registro de Reporte Ciudadano con Evidencia Fotográfica

Reporte offline-first de fugas en la vía pública o cortes imprevistos con coordenadas y fotografía adjunta.

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant UI as ReportesScreen
    participant FotoUtil as rememberCapturaFoto
    participant FileKit as rememberFilePickerLauncher
    participant UC as CrearReporte
    participant Repo as ReporteRepository (Fake/Room)
    participant Cola as ColaSincronizacionOffline

    Usuario->>UI: Selecciona tipo de incidencia ("FUGA EN VÍA PÚBLICA")
    Usuario->>UI: Ingresa descripción textual ("Rotura de tubería en Av. Bolognesi")
    
    alt Opción 1: Tomar Fotografía
        Usuario->>UI: Presiona "Tomar fotografía"
        UI->>FotoUtil: tomarFoto()
        FotoUtil->>Usuario: Abre cámara del dispositivo
        Usuario->>FotoUtil: Captura foto y confirma
        FotoUtil-->>UI: fotoAdjunta = true
    else Opción 2: Adjuntar de Galería
        Usuario->>UI: Presiona "Adjuntar de galería"
        UI->>FileKit: launch()
        FileKit->>Usuario: Selector de imágenes del sistema
        Usuario->>FileKit: Elige foto
        FileKit-->>UI: fotoAdjunta = true
    end

    Usuario->>UI: Presiona "Enviar Reporte"
    UI->>UC: ejecutar(Reporte(id, tipo, descripcion, coordenada, foto, fecha))
    activate UC
    UC->>Repo: guardar(reporte)
    activate Repo
    Repo->>Repo: Persiste reporte en SQLite local
    Repo->>Cola: Encolar para envío a Supabase cuando haya red
    Repo-->>UC: OK
    deactivate Repo
    UC-->>UI: Exito
    deactivate UC
    UI->>Usuario: Mensaje "Reporte registrado. Se enviará al recuperar conexión."
```

---

### 6.4 Exploración de Incidencias en el Mapa Comunitario

Visualización georreferenciada de reportes generados por la comunidad vecinal.

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant UI as ComunidadScreen
    participant Mapa as MapaReportes (Composable)
    participant Repo as ReporteRepository

    Usuario->>UI: Selecciona pestaña "Mapa Comunitario"
    UI->>Mapa: Carga componente de mapa
    activate Mapa
    Mapa->>Repo: obtenerReportesActivos()
    Repo-->>Mapa: List<Reporte> (Coordenadas, TipoReporte, Timestamp)
    loop Por cada reporte
        Mapa->>Mapa: Dibuja marcador temático (Gota roja para fugas, Alerta para cortes)
    end
    deactivate Mapa
    Mapa->>Usuario: Despliega mapa interactivo con clústeres de incidencias
    Usuario->>Mapa: Toca un marcador
    Mapa->>Usuario: Despliega ficha resumen de la incidencia comunitaria
```

---

## Resumen de Interacciones entre Módulos

El siguiente diagrama de alto nivel muestra cómo los módulos se comunican a través de los contratos de dominio sin violar la separación arquitectónica:

```mermaid
sequenceDiagram
    autonumber
    participant Sector as Módulo Sector
    participant Reserva as Módulo Reserva
    participant Recibo as Módulo Recibo
    participant Retos as Módulo Retos
    participant Asistente as Módulo Asistente

    Note over Sector,Reserva: Interdependencia Crítica:<br/>Reserva necesita el próximo turno de agua para calcular déficit
    Reserva->>Sector: AbastecimientosDeSector.proximoDesde(ahora)
    Sector-->>Reserva: ProximoAbastecimiento(fechaHora, horas)

    Note over Recibo,Reserva: Calibración de Consumo:<br/>El consumo histórico del recibo refina la tasa de consumo del hogar
    Reserva->>Recibo: ReciboRepository.obtenerUltimoConsumoM3()
    Recibo-->>Reserva: ConsumoPromedioMes

    Note over Reserva,Retos: Gamificación con Datos Reales:<br/>Retos compara el ahorro efectivo generado en la reserva
    Retos->>Reserva: ReservaRepository.litrosPorHabitanteDia()
    Reserva-->>Retos: LitrosPorHabitanteDia (ej. 92 L/hab/día)

    Note over Asistente,Recibo: Asistencia Guiada:<br/>El asistente n8n responde dudas sobre cobros y lectura de la boleta
    Asistente->>Recibo: Contexto del último recibo digitalizado
