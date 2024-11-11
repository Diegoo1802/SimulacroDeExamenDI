<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class pagina_web
    Inherits System.Windows.Forms.Form

    'Form reemplaza a Dispose para limpiar la lista de componentes.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Requerido por el Diseñador de Windows Forms
    Private components As System.ComponentModel.IContainer

    'NOTA: el Diseñador de Windows Forms necesita el siguiente procedimiento
    'Se puede modificar usando el Diseñador de Windows Forms.  
    'No lo modifique con el editor de código.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(pagina_web))
        Me.lbl_bodas = New System.Windows.Forms.Label()
        Me.lbl_comuniones = New System.Windows.Forms.Label()
        Me.lbl_bautizos = New System.Windows.Forms.Label()
        Me.PictureBox1 = New System.Windows.Forms.PictureBox()
        Me.PictureBox2 = New System.Windows.Forms.PictureBox()
        Me.PictureBox3 = New System.Windows.Forms.PictureBox()
        CType(Me.PictureBox1, System.ComponentModel.ISupportInitialize).BeginInit()
        CType(Me.PictureBox2, System.ComponentModel.ISupportInitialize).BeginInit()
        CType(Me.PictureBox3, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'lbl_bodas
        '
        Me.lbl_bodas.AutoSize = True
        Me.lbl_bodas.BackColor = System.Drawing.SystemColors.ActiveCaption
        Me.lbl_bodas.Font = New System.Drawing.Font("MV Boli", 15.75!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.lbl_bodas.Location = New System.Drawing.Point(606, 234)
        Me.lbl_bodas.Name = "lbl_bodas"
        Me.lbl_bodas.Size = New System.Drawing.Size(88, 28)
        Me.lbl_bodas.TabIndex = 0
        Me.lbl_bodas.Text = "BODAS"
        '
        'lbl_comuniones
        '
        Me.lbl_comuniones.AutoSize = True
        Me.lbl_comuniones.BackColor = System.Drawing.SystemColors.ActiveCaption
        Me.lbl_comuniones.Font = New System.Drawing.Font("MV Boli", 15.75!, System.Drawing.FontStyle.Bold)
        Me.lbl_comuniones.Location = New System.Drawing.Point(143, 64)
        Me.lbl_comuniones.Name = "lbl_comuniones"
        Me.lbl_comuniones.Size = New System.Drawing.Size(165, 28)
        Me.lbl_comuniones.TabIndex = 1
        Me.lbl_comuniones.Text = "COMUNIONES"
        '
        'lbl_bautizos
        '
        Me.lbl_bautizos.AutoSize = True
        Me.lbl_bautizos.BackColor = System.Drawing.SystemColors.ActiveCaption
        Me.lbl_bautizos.Font = New System.Drawing.Font("MV Boli", 15.75!, System.Drawing.FontStyle.Bold)
        Me.lbl_bautizos.Location = New System.Drawing.Point(579, 64)
        Me.lbl_bautizos.Name = "lbl_bautizos"
        Me.lbl_bautizos.Size = New System.Drawing.Size(127, 28)
        Me.lbl_bautizos.TabIndex = 2
        Me.lbl_bautizos.Text = "BAUTIZOS"
        '
        'PictureBox1
        '
        Me.PictureBox1.Image = CType(resources.GetObject("PictureBox1.Image"), System.Drawing.Image)
        Me.PictureBox1.Location = New System.Drawing.Point(563, 290)
        Me.PictureBox1.Name = "PictureBox1"
        Me.PictureBox1.Size = New System.Drawing.Size(177, 120)
        Me.PictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom
        Me.PictureBox1.TabIndex = 3
        Me.PictureBox1.TabStop = False
        '
        'PictureBox2
        '
        Me.PictureBox2.Enabled = False
        Me.PictureBox2.Image = CType(resources.GetObject("PictureBox2.Image"), System.Drawing.Image)
        Me.PictureBox2.Location = New System.Drawing.Point(563, 123)
        Me.PictureBox2.Name = "PictureBox2"
        Me.PictureBox2.Size = New System.Drawing.Size(177, 93)
        Me.PictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom
        Me.PictureBox2.TabIndex = 4
        Me.PictureBox2.TabStop = False
        '
        'PictureBox3
        '
        Me.PictureBox3.Image = CType(resources.GetObject("PictureBox3.Image"), System.Drawing.Image)
        Me.PictureBox3.Location = New System.Drawing.Point(24, 123)
        Me.PictureBox3.Name = "PictureBox3"
        Me.PictureBox3.Size = New System.Drawing.Size(443, 287)
        Me.PictureBox3.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom
        Me.PictureBox3.TabIndex = 5
        Me.PictureBox3.TabStop = False
        '
        'pagina_web
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(800, 450)
        Me.Controls.Add(Me.PictureBox3)
        Me.Controls.Add(Me.PictureBox2)
        Me.Controls.Add(Me.PictureBox1)
        Me.Controls.Add(Me.lbl_bautizos)
        Me.Controls.Add(Me.lbl_comuniones)
        Me.Controls.Add(Me.lbl_bodas)
        Me.MaximizeBox = False
        Me.MinimizeBox = False
        Me.Name = "pagina_web"
        Me.Text = "BBCs"
        CType(Me.PictureBox1, System.ComponentModel.ISupportInitialize).EndInit()
        CType(Me.PictureBox2, System.ComponentModel.ISupportInitialize).EndInit()
        CType(Me.PictureBox3, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents lbl_bodas As Label
    Friend WithEvents lbl_comuniones As Label
    Friend WithEvents lbl_bautizos As Label
    Friend WithEvents PictureBox1 As PictureBox
    Friend WithEvents PictureBox2 As PictureBox
    Friend WithEvents PictureBox3 As PictureBox
End Class
