Declare @Date datetime
Declare @Success nchar(10)
Declare @Failure nchar (10)

SET @Date = getdate()
SET @Success = 'S'
SET @Failure = 'F'


Insert into [Admin].[_backup_logs] ([Date], [Failure])
Select @Date, @Failure