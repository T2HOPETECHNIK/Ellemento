import {inject, Getter} from '@loopback/core';
import {DefaultCrudRepository, repository, HasOneRepositoryFactory, BelongsToAccessor} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {History, HistoryRelations, TrayMovement, TrayWashing, Potting, Transplanting} from '../models';
import {TrayMovementRepository} from './tray-movement.repository';
import {TrayWashingRepository} from './tray-washing.repository';
import {PottingRepository} from './potting.repository';
import {TransplantingRepository} from './transplanting.repository';

export class HistoryRepository extends DefaultCrudRepository<
  History,
  typeof History.prototype.history_id,
  HistoryRelations
> {

  public readonly trayMovement: HasOneRepositoryFactory<TrayMovement, typeof History.prototype.history_id>;

  public readonly trayWashing: HasOneRepositoryFactory<TrayWashing, typeof History.prototype.history_id>;

  public readonly potting: HasOneRepositoryFactory<Potting, typeof History.prototype.history_id>;

  public readonly transplanting: HasOneRepositoryFactory<Transplanting, typeof History.prototype.history_id>;

  public readonly trayActionTableId: BelongsToAccessor<Potting, typeof History.prototype.history_id>;

  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource, @repository.getter('TrayMovementRepository') protected trayMovementRepositoryGetter: Getter<TrayMovementRepository>, @repository.getter('TrayWashingRepository') protected trayWashingRepositoryGetter: Getter<TrayWashingRepository>, @repository.getter('PottingRepository') protected pottingRepositoryGetter: Getter<PottingRepository>, @repository.getter('TransplantingRepository') protected transplantingRepositoryGetter: Getter<TransplantingRepository>,
  ) {
    super(History, dataSource);
    this.trayActionTableId = this.createBelongsToAccessorFor('trayActionTableId', pottingRepositoryGetter,);
    this.registerInclusionResolver('trayActionTableId', this.trayActionTableId.inclusionResolver);
    this.transplanting = this.createHasOneRepositoryFactoryFor('transplanting', transplantingRepositoryGetter);
    this.registerInclusionResolver('transplanting', this.transplanting.inclusionResolver);
    this.potting = this.createHasOneRepositoryFactoryFor('potting', pottingRepositoryGetter);
    this.registerInclusionResolver('potting', this.potting.inclusionResolver);
    this.trayWashing = this.createHasOneRepositoryFactoryFor('trayWashing', trayWashingRepositoryGetter);
    this.registerInclusionResolver('trayWashing', this.trayWashing.inclusionResolver);
    this.trayMovement = this.createHasOneRepositoryFactoryFor('trayMovement', trayMovementRepositoryGetter);
    this.registerInclusionResolver('trayMovement', this.trayMovement.inclusionResolver);
  }
}
